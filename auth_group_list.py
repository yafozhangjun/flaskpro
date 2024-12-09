import hashlib
import json
import pyodbc
from flask import Flask, request, jsonify, Blueprint
from common.database_config import *
from common.public_method import *
from datetime import datetime, time

from models import SysAuthGroup
from utils import common


from flask import Flask, jsonify
import pyodbc

authGroup = Blueprint('authGroup', __name__)


# 查询权限列表
@authGroup.route('/authGroupList', methods=['GET'])
def authGroupList_index():
    state = request.args.get('state', '1', type=int)
    title = request.args.get('title', type=str)
    get_filter_list = request.args.get('getFilterList', type=str) == 'true'

    rel = SysAuthGroup.query.filter_by(status=state).order_by(SysAuthGroup.addTime.desc())

    if title:
        rel = rel.filter(SysAuthGroup.title.ilike(f'%{title}%'))

    if get_filter_list:
        data = common.to_array_list(rel)
    else:
        page_size = request.args.get('pageSize', 10, type=int)
        page_num = request.args.get('pageNum', 1, type=int)
        json_data = common.paginate_query(rel, page_num, page_size)
        data = {'list': json_data, 'pageSize': page_size, 'pageNum': page_num, 'total': rel.count()}

    response_data = {'success': 1, 'message': '请求成功', 'data': data}
    return jsonify(response_data)

@authGroup.route('/addAuthGroup', methods=['POST'])
def addAuthGroup_index():
    data = request.get_json()  # 获取JSON数据

    # 名称
    title = data.get("title")
    if not title:
        return jsonify({'success': 0, 'message': 'title不能为空'}),401

    # 路由
    rules = data.get("rules")
    if not rules:
        return jsonify({'success': 0, 'message': 'rules不能为空'}),401

    # 状态
    status = data.get("status")
    if not (isinstance(status, int) and status >= 0):
        status = 1

    # 操作员id
    userId = data.get("userId")
    if not userId:
        return jsonify({'success': 0, 'message': 'userId不能为空'}),401

    # 添加时间
    now_time = datetime.now()
    addtime = now_time.strftime('%Y-%m-%d %H:%M:%S')

    # 创建对象
    new_group = SysAuthGroup(title=title, rules=rules, status=status, userId=userId, addTime=addtime)
    db.session.add(new_group)
    db.session.commit()

    response_data = {'success': 1, 'message': '成功'}
    return jsonify(response_data),500

@authGroup.route('/saveAuthGroup', methods=['POST'])
def saveAuthGroup_index():
    data = request.get_json()  # 获取JSON数据

    # id
    id = data.get("id")
    if not id:
        return jsonify({'success': 0, 'message': 'id不能为空'}),401

    # 名称
    title = data.get("title")
    if not title:
        return jsonify({'success': 0, 'message': 'title不能为空'}),401

    # 路由
    rules = data.get("rules")
    if not rules:
        return jsonify({'success': 0, 'message': 'rules不能为空'}),401

    # 状态
    status = data.get("status")
    if not (isinstance(status, int) and status >= 0):
        status = 1

    # 更新对象
    update_obj = SysAuthGroup.query.get(id)
    if not update_obj:
        return jsonify({'success': 0, 'message': '未找到指定的权限组'}),401

    update_obj.title = title
    update_obj.rules = rules
    update_obj.status = status
    db.session.commit()  # 提交更改到数据库

    return jsonify({'success': 1, 'message': '成功'})


@authGroup.route('/delAuthGroup', methods=['POST'])
def delAuthGroup_index():
    data = request.get_json()  # 获取JSON数据
    group_ids = data.get("id")

    if not group_ids:
        return jsonify({'success': 0, 'message': 'id不能为空'}),401

    if isinstance(group_ids, int):
        # 如果是单个ID，直接删除
        SysAuthGroup.query.filter_by(id=group_ids).delete()
    else:
        # 如果是多个ID，使用in_()方法来删除多个
        SysAuthGroup.query.filter(SysAuthGroup.id.in_(group_ids)).delete()

    db.session.commit()  # 提交更改到数据库

    return jsonify({'success': 1, 'message': '成功'})
