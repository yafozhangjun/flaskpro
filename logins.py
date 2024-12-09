import hashlib
import json



import pyodbc
from flask import Flask, request, jsonify, Blueprint
from common.database_config import *
from common.public_method import *
from datetime import datetime
import time

from models import SysUser, SysUserToken
from utils.common import to_array_list, make_dict, model_to_dict

register = Blueprint('register', __name__)
login = Blueprint('login', __name__)
checkLogin = Blueprint('checkLogin', __name__)

def md5(user):
    """生成用户token"""
    ctime = str(time.time())
    m = hashlib.md5()
    m.update(str(user).encode('utf-8'))  # 将用户名转换为字节后更新md5对象
    m.update(ctime.encode('utf-8'))  # 将时间戳转换为字节后更新md5对象
    return m.hexdigest()  # 返回加密后的字符串


# 验证登录
@register.route('/checkLogin', methods=['POST'])
def check_login():
    username = request.json.get('userName')
    if not username or username.strip() == "":
        return jsonify({'success': 0, 'msg': '用户名不能为空'}), 401
    password = request.json.get('passWord')
    if not password or password.strip() == "":
        return jsonify({'success': 0, 'msg': '密码不能为空'}), 401
    try:
        # 连接数据库
        cnx = pyodbc.connect(DATABASE_CONFIG)
        cursor = cnx.cursor()
    except Exception as err:
        print("Error decoding config file: %s" % str(err))

    query = "SELECT * FROM tht.sys_user WHERE userName = @userName AND passWord = @passWord"
    parameters = {'userName': username, 'passWord': password}
    cursor.execute(query, parameters)
    row = cursor.fetchone()
    # 如果是插入、删除、更新语句切记要写提交命令con.commit()
    cursor.close()
    cnx.close()
    user = row
    if user:
        # 登录成功
        # 1，生成特殊字符串
        # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
        # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
        # request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
        # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id

        user_str = {
            'userId': '',
            'userName': '',
            'realName': '',
            'roleId': '',
            'telePhone': '',
            'address': ''
        }
        i = 0
        for temp in user_str:
            user_str[temp] = user[i]
            print(user_str[temp])
            i = i + 1
        user_str['ok'] = 'ok'
        user_str = json.dumps(user_str)

        return jsonify({'success': 1, 'msg': '登陆成功','data':user_str}), 200
    else:
        return jsonify({'success': 1, 'msg': '用户名或密码错误'}), 401

# 验证登录
@register.route('/login', methods=['POST'])
def login_index():
    if request.data:
        data = json.loads(request.data)
        userName = data.get('userName')
        passWord = data.get('passWord')

        if not userName or not passWord:
            return jsonify({'success': 0, 'message': '用户名密码不能为空', 'data': {}})

        sys_user = SysUser.query.filter_by(userName=userName, passWord=passWord).first()
        if not sys_user:
            return jsonify({'success': 0, 'message': '用户名密码错误', 'data': {}})

        # 创建唯一的用户token
        token = hashlib.md5(passWord.encode()).hexdigest()
        now = datetime.now()
        sys_user_token = SysUserToken.query.filter_by(userId=sys_user.userId).first()
        if sys_user_token:
            sys_user_token.token = token
            sys_user_token.update_time = now
            db.session.commit()
        else:
            sys_user_token = SysUserToken(userId=sys_user.userId, roleId=sys_user.roleid, token=token, update_time=now)
            db.session.add(sys_user_token)
            db.session.commit()
        sys_user_data = model_to_dict(sys_user)
        data = {
            'userId': sys_user.userId,
            'token': token,
            'list': [sys_user_data],
            'pageSize': 100,
            'pageNum': 1,
            'total': 1,
        }
        return jsonify({'success': 1, 'message': '登录成功', 'data': data})
    else:
        return jsonify({'success': 0, 'message': '用户名密码不能为空', 'data': {}})



