import hashlib
import json
import pyodbc
from flask import Flask, request, jsonify, Blueprint
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

from common.database_config import *
from common.marshmallow import model_to_dict
from common.public_method import *
from datetime import datetime, time

from models import SysAuthRule, SysUser, SysAuthGroup
from utils import common
from utils.common import build_tree
# from verification_code import in_click


from flask import Flask, jsonify
import pyodbc

authRule = Blueprint('authRule', __name__)
authRuleList = Blueprint('authRuleList', __name__)
addAuthRule = Blueprint('addAuthRule', __name__)
saveAuthRule = Blueprint('saveAuthRule', __name__)
delAuthRule = Blueprint('delAuthRule', __name__)
userList = Blueprint('userList', __name__)
addUser = Blueprint('addUser', __name__)
saveUser = Blueprint('saveUser', __name__)
delUser = Blueprint('delUser', __name__)
getMenuList = Blueprint('getMenuList', __name__)

# 查询路由
@authRule.route('/authRuleList', methods=['GET'])
def auth_rule_list():
    rel = SysAuthRule.query.order_by(SysAuthRule.sort.desc()).all()
    rel_values = [row.__dict__ for row in rel]
    for row in rel_values:
        row.pop('_sa_instance_state', None)  # 移除 SQLAlchemy 的内部状态字段

    data = build_tree(rel_values)
    response_data = {'success': 1, 'message': '请求成功', 'data': {'list': data}}
    return jsonify(response_data)

# 新增路由
@authRule.route('/addAuthRule', methods=['POST'])
def addAuthRule_index():
    data = request.get_json()

    # 提取参数
    rule_title = data.get("title")
    rule_pid = data.get("pid")
    rule_path = data.get("path")
    rule_name = data.get("name")
    rule_redirect = data.get("redirect")
    rule_component = data.get("component")
    rule_icon = data.get("icon")
    rule_islink = data.get("isLink", False)
    rule_ishide = data.get("isHide", False)
    rule_isfull = data.get("isFull", False)
    rule_isaffix = data.get("isAffix", False)
    rule_iskeepalive = data.get("isKeepAlive", False)
    rule_isadd = data.get("isAdd", True)
    rule_isedit = data.get("isEdit", True)
    rule_isdel = data.get("isDel", True)
    rule_minipage = data.get("miniPage")
    rule_miniicon = data.get("miniIcon")
    rule_image = data.get("image")

    # 创建新的SysAuthRule对象
    new_rule = SysAuthRule(
        title=rule_title,
        pid=rule_pid,
        path=rule_path,
        name=rule_name,
        redirect=rule_redirect,
        component=rule_component,
        icon=rule_icon,
        isLink=rule_islink,
        isHide=rule_ishide,
        isFull=rule_isfull,
        isAffix=rule_isaffix,
        isKeepAlive=rule_iskeepalive,
        isAdd=rule_isadd,
        isEdit=rule_isedit,
        isDel=rule_isdel,
        miniPage=rule_minipage,
        miniIcon=rule_miniicon,
        image=rule_image
    )
    db.session.add(new_rule)
    db.session.commit()

    response_data = {'success': 1, 'message': '成功'}
    return jsonify(response_data)


# 修改路由
@authRule.route('/saveAuthRule', methods=['POST'])
def SaveAuthRule_index():
    data = request.get_json()
    id = data.get('id')
    if not id:
        return jsonify({'success': 0, 'message': 'id不能为空'})

    title = data.get('title')
    if not title:
        return jsonify({'success': 0, 'message': 'title不能为空'})

    pid = data.get('pid')
    if not str(pid).isnumeric() or int(pid) < 0:
        return jsonify({'success': 0, 'message': 'pid不能为空'})

    path = data.get('path')
    if not path:
        return jsonify({'success': 0, 'message': 'path不能为空'})

    name = data.get('name')
    if not name:
        return jsonify({'success': 0, 'message': 'name不能为空'})

    redirect = data.get('redirect') if data.get('redirect') is not None else None
    component = data.get('component') if data.get('component') is not None else None
    icon = data.get('icon') if data.get('icon') is not None else None
    isLink = data.get('isLink') if data.get('isLink') is not None else 0
    isHide = data.get('isHide') if data.get('isHide') is not None else 0
    isFull = data.get('isFull') if data.get('isFull') is not None else 0
    isAffix = data.get('isAffix') if data.get('isAffix') is not None else 0
    isKeepAlive = data.get('isKeepAlive') if data.get('isKeepAlive') is not None else 0
    isAdd = data.get('isAdd') if data.get('isAdd') is not None else 1
    isEdit = data.get('isEdit') if data.get('isEdit') is not None else 1
    isDel = data.get('isDel') if data.get('isDel') is not None else 1
    miniPage = data.get('miniPage') if data.get('miniPage') is not None else None
    miniIcon = data.get('miniIcon') if data.get('miniIcon') is not None else None
    image = data.get('image') if data.get('image') is not None else None

    try:
        auth_rule = SysAuthRule.query.filter_by(id=id).first()
        if not auth_rule:
            return jsonify({'success': 0, 'message': 'No record found with the provided id'})

        auth_rule.title = title
        auth_rule.pid = pid
        auth_rule.path = path
        auth_rule.name = name
        auth_rule.redirect = redirect
        auth_rule.component = component
        auth_rule.icon = icon
        auth_rule.isLink = isLink
        auth_rule.isHide = isHide
        auth_rule.isFull = isFull
        auth_rule.isAffix = isAffix
        auth_rule.isKeepAlive = isKeepAlive
        auth_rule.isAdd = isAdd
        auth_rule.isEdit = isEdit
        auth_rule.isFull = isFull
        auth_rule.isDel = isDel
        auth_rule.miniPage = miniPage
        auth_rule.miniIcon = miniIcon
        auth_rule.image = image
        db.session.commit()
        return jsonify({'success': 1, 'message': '成功'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'success': 0, 'message': str(e)})

# 删除路由
@authRule.route('/delAuthRule', methods=['POST'])
def delAuthRule_index():
    try:
        # 解析请求体
        rel = request.json
        id_list = rel.get("id")
        if not id_list:
            return jsonify({'success': 0, 'message': 'id不能为空'}), 400

        if isinstance(id_list, int):
            # 如果是单个ID，直接删除
            SysAuthRule.query.filter_by(id=id_list).delete()
        else:
            # 如果是多个ID，使用in_()方法来删除多个
            SysAuthRule.query.filter(SysAuthRule.id.in_(id_list)).delete()

        db.session.commit()  # 提交更改到数据库
        # 返回响应
        response_data = {'success': 1, 'message': '成功'}
        return jsonify(response_data), 200

    except Exception as e:
        response_data = {'success': 0, 'message': '失败', 'error': str(e)}
        return jsonify(response_data), 500

# 用户列表信息
@authRule.route('/userList', methods=['GET'])
def userList_index():
    # 状态：0 禁用，1 启用
    state = request.args.get('state', '1')
    rel = SysUser.query.filter_by(state=state).order_by(desc(SysUser.addTime))

    # 筛选条件
    username = request.args.get('username')
    if username:
        rel = rel.filter(SysUser.userName.ilike(f'%{username}%'))

    # userid
    userid = request.args.get('userid')
    if userid:
        rel = rel.filter_by(userId=userid)

    # 是否获取筛选列表
    get_filter_list = request.args.get("getFilterList", "false").lower() == "true"
    if get_filter_list:
        data = common.to_array_list(rel)
    else:
        # 分页
        page_size = int(request.args.get("pageSize", 10))
        page_num = int(request.args.get("pageNum", 1))
        json_data = common.paginate_query(rel,page_num,page_size)
        data = {'list': json_data, 'pageSize': page_size, 'pageNum': page_num, 'total': rel.count()}

    response_data = {'success': 1, 'message': '请求成功', 'data': data}
    return jsonify(response_data)

# 新增用户
@authRule.route('/addUser', methods=['POST', 'GET'])
def addUser_index():
    if request.method == 'POST':
        try:
            rel = request.get_json()
            username = rel.get("username")
            if not username:
                return jsonify({'success': 0, 'message': 'username不能为空'})

            realname = rel.get("realname")
            if not realname:
                return jsonify({'success': 0, 'message': 'realname不能为空'})

            password = rel.get("password")
            if not password:
                return jsonify({'success': 0, 'message': 'password不能为空'})

            roleid = rel.get("roleid")
            if not roleid:
                return jsonify({'success': 0, 'message': 'roleid不能为空'})

            telephone = rel.get("telephone")
            if not telephone:
                return jsonify({'success': 0, 'message': 'telephone不能为空'})

            address = rel.get("address")
            if not address:
                return jsonify({'success': 0, 'message': 'address不能为空'})

            field_operatorid = rel.get("field_operatorid")
            if not field_operatorid:
                return jsonify({'success': 0, 'message': 'field_operatorid不能为空'})

            state = 1 if rel.get("state") else 0
            teamid = rel.get("teamid")
            teamid = f"'{teamid}'" if teamid else 'NULL'

            now_time = datetime.now()
            addtime = now_time.strftime('%Y-%m-%d %H:%M:%S')

            # Connect to the database using pyodbc
            cnx = pyodbc.connect(DATABASE_CONFIG)  # Update with your actual database configuration
            cursor = cnx.cursor()

            # Check if the user already exists
            cursor.execute("SELECT COUNT(*) FROM sys_user WHERE username = ?", (username,))
            exists = cursor.fetchone()[0]
            if exists:
                return jsonify({'success': 0, 'message': '该用户已存在'})

            # Insert the new user
            cursor.execute("""
                INSERT INTO sys_user (username, realname, password, roleid, telephone, address, field_operatorid, addtime, state, teamid)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (username, realname, password, roleid, telephone, address, field_operatorid, addtime, state, teamid))

            # Commit the changes and close the connection
            cnx.commit()
            cursor.close()
            cnx.close()

            return jsonify({'success': 1, 'message': '成功'})

        except Exception as e:
            return jsonify({'success': 0, 'message': str(e)}), 401

    elif request.method == 'GET':
        return jsonify({'success': 1, 'message': '请求成功', 'data': []})

# 修改用户权限
@authRule.route('/saveUser', methods=['POST', 'GET'])
def saveUser_index():
    if request.method == 'POST':
        try:
            rel = request.get_json()
            userid = rel.get("userid")
            if not userid:
                return jsonify({'success': 0, 'message': 'userid不能为空'})

            username = rel.get("username")
            if not username:
                return jsonify({'success': 0, 'message': 'username不能为空'})

            realname = rel.get("realname")
            if not realname:
                return jsonify({'success': 0, 'message': 'realname不能为空'})

            password = rel.get("password")
            if not password:
                return jsonify({'success': 0, 'message': 'password不能为空'})

            roleid = rel.get("roleid")
            if not roleid:
                return jsonify({'success': 0, 'message': 'roleid不能为空'})

            telephone = rel.get("telephone")
            if not telephone:
                return jsonify({'success': 0, 'message': 'telephone不能为空'})

            address = rel.get("address")
            if not address:
                return jsonify({'success': 0, 'message': 'address不能为空'})

            state = 1 if rel.get("state") else 0
            teamid = rel.get("teamid")
            teamid = f"'{teamid}'" if teamid else 'NULL'

            # Connect to the database using pyodbc
            cnx = pyodbc.connect(DATABASE_CONFIG)  # Update with your actual database configuration
            cursor = cnx.cursor()

            # Update the user
            cursor.execute("""
                UPDATE sys_user
                SET username = ?, realname = ?, password = ?, roleid = ?, telephone = ?, address = ?, state = ?, teamid = ?
                WHERE userid = ?
            """, (username, realname, password, roleid, telephone, address, state, teamid, userid))

            # Commit the changes and close the connection
            cnx.commit()
            cursor.close()
            cnx.close()

            return jsonify({'success': 1, 'message': '成功'})

        except Exception as e:
            return jsonify({'success': 0, 'message': str(e)}), 401

    elif request.method == 'GET':
        return jsonify({'success': 1, 'message': '请求成功', 'data': []})

# 删除用户权限
@authRule.route('/delUser', methods=['POST', 'GET'])
def delUser_index():
    if request.method == 'POST':
        try:
            rel = request.get_json()
            userid = rel.get("userid")
            if not userid:
                return jsonify({'success': 0, 'message': 'userid不能为空'})

            # Super admin check (assuming the super admin has the userid of 1)
            if userid == 1:
                return jsonify({'success': 0, 'message': '超级管理员不能删除'})

            # Connect to the database using pyodbc
            cnx = pyodbc.connect(DATABASE_CONFIG)  # Update with your actual database configuration
            cursor = cnx.cursor()

            # Delete the user or list of users
            if isinstance(userid, list):
                # Delete multiple users
                placeholders = ', '.join('?' for unused in userid)
                cursor.execute(f"DELETE FROM sys_user WHERE userid IN ({placeholders})", userid)
            else:
                # Delete a single user
                cursor.execute("DELETE FROM sys_user WHERE userid = ?", (userid,))

            # Commit the changes and close the connection
            cnx.commit()
            cursor.close()
            cnx.close()

            return jsonify({'success': 1, 'message': '成功'})

        except Exception as e:
            return jsonify({'success': 0, 'message': str(e)}), 401

    elif request.method == 'GET':
        return jsonify({'success': 1, 'message': '请求成功', 'data': []})

# 菜单树结构列表
@authRule.route('/getMenuList', methods=['POST', 'GET'])
def getMenuList_index():
    if request.method == 'POST':
        rel = json.loads(request.data)
        if rel.get("userId"):
            userId = rel.get("userId")
        else:
            return jsonify({'success': 0, 'message': 'userid不能为空'})

        menuData = SysAuthRule.query.all()
        userData = SysUser.query.filter_by(userId=userId).all()
        ruleIdList = {}

        for item in userData:
            ruleData = SysAuthGroup.query.filter_by(id=item.roleId).all()
            for row in ruleData:
                ruleIdList = row.rules.split(',')
        data = []
        # menuData =  json.dumps(model_to_dict(menuData))
        for menu in menuData:
            if str(menu.id) in ruleIdList:
                setData = menu.__dict__
                del setData['_sa_instance_state']
                data.append(setData)

        treeData = build_tree(data)
        response_data = {'success': 1, 'message': '请求成功', 'data': {'list': treeData}}
        return jsonify(response_data)

    else:
        response_data = {'success': 1, 'message': '请求成功', 'data': []}
        return jsonify(response_data)
