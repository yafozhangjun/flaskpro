import hashlib
import json



import pyodbc
from flask import Flask, request, jsonify, Blueprint
from common.database_config import *
from common.public_method import *
from datetime import datetime
import time

from models import SysDictionary, SysUser, SysOperationLog, SysAuthGroup
from utils import common
from utils.common import to_array_list, paginate_query

dictionarys = Blueprint('dictionarys', __name__)
dicList = Blueprint('dicList', __name__)
addDic = Blueprint('addDic', __name__)
saveDic = Blueprint('saveDic', __name__)
delDic = Blueprint('delDic', __name__)
editPassword = Blueprint('editPassword', __name__)
operationLog = Blueprint('operationLog', __name__)
addProjectGroup = Blueprint('addProjectGroup', __name__)

# 获取字典
@dictionarys.route('/dictionary/dicList', methods=['GET'])
def dictionary_index():
    cnx  = ""
    cursor = ""
    try:
        dicData = SysDictionary.query
        dicData = to_array_list(dicData)
        dicData = common.build_tree(dicData)

        return jsonify({'success': 1, 'message': '请求成功', 'data': dicData}), 200
    except Exception as err:
        return jsonify({'success': 0, 'msg': '参数错误','error':err}), 401

# 添加字典
@dictionarys.route('/dictionary/addDic', methods=['POST'])
def addDic_index():
    data = json.loads(request.data)
    if 'pid' in data and str(data['pid']).isnumeric() and int(data['pid']) >= 0:
        pid = data['pid']
    else:
        return jsonify({'success': 0, 'message': 'pid不能为空'}), 400

    if 'workName' in data and data['workName']:
        workName = data['workName']
    else:
        return jsonify({'success': 0, 'message': 'workname不能为空'}), 400

    workCode = data.get('workCode')
    note = data.get('note')
    now_time = datetime.now()
    addTime = now_time.strftime('%Y-%m-%d %H:%M:%S')

    check = SysDictionary.query.filter_by(workName=workName, pid=pid).first()
    if check:
        return jsonify({'success': 0, 'message': '该字典已存在'}), 400
    else:
        new_entry = SysDictionary(pid=pid, workName=workName, workCode=workCode, note=note, addTime=addTime)
        db.session.add(new_entry)
        db.session.commit()

    return jsonify({'success': 1, 'message': '成功'})

# 修改字典
@dictionarys.route('/dictionary/saveDic', methods=['POST'])
def saveDic_index():
    data = json.loads(request.data)

    id = data.get('id')
    if not id:
        return jsonify({'success': 0, 'message': 'id不能为空'}), 400

    pid = data.get('pid')
    if not pid or not str(pid).isnumeric() or int(pid) < 0:
        return jsonify({'success': 0, 'message': 'pid不能为空'}), 400

    workName = data.get('workName')
    if not workName:
        return jsonify({'success': 0, 'message': 'workName不能为空'}), 400

    workCode = data.get('workCode')
    note = data.get('note')

    # Check if the dictionary already exists with the same workname and pid, excluding the current id
    check = SysDictionary.query.filter_by(workName=workName, pid=pid).filter(SysDictionary.id != id).first()
    if check:
        return jsonify({'success': 0, 'message': '该字典已存在'}), 400

    # Update the existing dictionary
    sys_dict = SysDictionary.query.filter_by(id=id).first()
    if sys_dict:
        sys_dict.pid = pid
        sys_dict.workName = workName
        sys_dict.workCode = workCode
        sys_dict.note = note
        db.session.commit()
        return jsonify({'success': 1, 'message': '成功'})
    else:
        return jsonify({'success': 0, 'message': '字典不存在，无法更新'}), 404

# 删除字典
@dictionarys.route('/dictionary/delDic', methods=['POST'])
def delDic_index():
    data = json.loads(request.data)
    del_list = data.get('id')
    if not del_list:
        return jsonify({'success': 0, 'message': 'id不能为空'}), 400

    # Determine if del_list is a single integer or a list of integers
    if isinstance(del_list, int):
        del_list = [del_list]

    # Delete records where id or pid matches any value in del_list
    SysDictionary.query.filter((SysDictionary.id.in_(del_list)) | (SysDictionary.pid.in_(del_list))).delete(
        synchronize_session=False)
    db.session.commit()

    return jsonify({'success': 1, 'message': '成功'})



# 修改密码
@dictionarys.route('/dictionary/editPassword', methods=['POST'])
def editPassword_index():
    data = json.loads(request.data)
    userId = data.get('userId')
    if not userId:
        return jsonify({'success': 0, 'message': 'userId不能为空'}), 400

    old_password = data.get('oldPassword')
    if not old_password:
        return jsonify({'success': 0, 'message': 'oldPassword不能为空'}), 400

    user_data = SysUser.query.filter_by(userId=userId).first()
    if not user_data:
        return jsonify({'success': 0, 'message': 'oldPassword输入错误！'}), 400

    new_password = data.get('newPassword')
    if not new_password:
        return jsonify({'success': 0, 'message': 'newPassword不能为空'}), 400

    new2_password = data.get('new2Password')
    if not new2_password:
        return jsonify({'success': 0, 'message': 'new2Password不能为空'}), 400

    if old_password == new_password:
        return jsonify({'success': 0, 'message': '新旧密码不能一致！'}), 400

    if new_password != new2_password:
        return({'success': 0, 'message': '新密码不一致！'}), 400

    # Hash the new password before storing it
    user_data.password = new_password
    db.session.commit()

    return jsonify({'success': 1, 'message': '成功'})

# 操作日志
@dictionarys.route('/dictionary/operationLog', methods=['POST'])
def operationLog_index():
    query_set = SysOperationLog.query.order_by(SysOperationLog.add_time.desc())
    userName = request.args.get('userName')
    if userName:
        user_ids = SysUser.query.filter(SysUser.userName.contains(userName)).with_entities(SysUser.userId).all()
        query_set = query_set.filter(SysOperationLog.user_id.in_(user_ids))

    start_time = request.args.get('startTime')
    if start_time:
        query_set = query_set.filter(SysOperationLog.add_time >= start_time)

    end_time = request.args.get('endTime')
    if end_time:
        query_set = query_set.filter(SysOperationLog.add_time <= end_time)

    get_filter_list = request.args.get("getFilterList")
    if get_filter_list:
        data = to_array_list(query_set)
    else:
        # 分页
        page_size = int(request.args.get("pageSize", 10))
        page_num = int(request.args.get("pageNum", 1))
        json_data = paginate_query(query_set,page_num,page_size )

        # 为每个数据项添加username字段
        for jd in json_data:
            user = SysUser.query.get(userId=jd['user_id'])
            if user:
                jd['userName'] = user.userName
            else:
                jd['username'] = None  # 或者适当的默认值

        data = {
            'list': json_data,
            'pageSize': page_size,
            'pageNum': page_num,
            'total': query_set.count()
        }
    response_data = {'success': 1, 'message': '请求成功', 'data': data}
    return jsonify(response_data)

# 角色添加项目权限
@dictionarys.route('/dictionary/addProjectGroup', methods=['POST'])
def addProjectGroup_index():
    data = json.loads(request.data)

    id = data.get('id')
    if not id:
        return jsonify({'success': 0, 'message': 'id不能为空'}), 400

    projectGroup = data.get('projectGroup')
    if projectGroup is not None:
        # Ensure that projectgroup is a list and join it into a string
        projectGroup = ','.join(str(i) for i in projectGroup)

    # Update the SysAuthGroup record
    sys_auth_group = SysAuthGroup.query.filter_by(id=id).first()
    if sys_auth_group:
        sys_auth_group.projectGroup = projectGroup
        db.session.commit()
        response_data = {'success': 1, 'message': '成功'}
    else:
        response_data = {'success': 0, 'message': '记录不存在，无法更新'}

    return jsonify(response_data)
