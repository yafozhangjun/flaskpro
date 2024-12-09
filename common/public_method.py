from flask import jsonify, request
import jwt
import mysql.connector
from mysql.connector import Error
from common.common import public_systems   # 导入公共文件
from common.database_config import *  # 导入数据库配置
from datetime import datetime, timedelta


def verify_token():
    token = request.headers.get('Authorization')
    if not token:
        return None, jsonify({'success': 0, 'errCode': 403, 'msg': '登录失效，请重新登录'}), 403

    try:
        # 检查Redis中的token是否被标记为无效
        if is_in_blacklist(token):
            return None, jsonify({'success': 0, 'errCode': 403, 'msg': '登录失效，请重新登录'}), 403

        payload = jwt.decode(token, public_systems['SECRET_KEY'], algorithms=public_systems['ALGORITHM'])
        if not payload.get('userId'):
            return None, jsonify({'success': 0, 'errCode': 403, 'msg': '登录错误，请重新登录'}), 403

        user_data = {'user_id': payload.get('userId'), 'username': payload.get('username'), 'is_visitor': payload.get('is_visitor')}
        return user_data, None, None

    except jwt.ExpiredSignatureError:
        # 修改登录状态
        editLoginState(token)

        remove_from_blacklist(token)
        return None, jsonify({'success': 0, 'errCode': 403, 'msg': '登录已超时，请重新登录'}), 403
    except jwt.InvalidTokenError:
        return None, jsonify({'success': 0, 'errCode': 403, 'msg': '登录错误，请重新登录'}), 403
    except Exception as e:
        print(e)
        return None, jsonify({'success': 0, 'errCode': 500, 'msg': '发生未知错误，请重试'}), 500


# 添加黑名单项到Redis集合中
def add_to_blacklist(item):
    redis_client.sadd('blacklist', item)


# 从黑名单中移除项
def remove_from_blacklist(item):
    redis_client.srem('blacklist', item)
    redis_client.delete(item)


# 检查项是否在黑名单中
def is_in_blacklist(item):
    return redis_client.sismember('blacklist', item)


# 修改登录状态
def editLoginState(token):
    uid = redis_client.get(token)
    if uid:
        res_data, sql_error = execute_query("UPDATE users SET is_login = 0, token = null WHERE id = %s", (uid,))
        if sql_error:
            return sql_error


# 登录校验
def is_token_expired(token, leeway=0):
    """
    检查JWT是否过期。

    :param token: JWT字符串
    :param secret_key: 用于签名JWT的密钥
    :param algorithm: 签名算法，默认为HS256
    :param leeway: 允许的过期时间偏差（秒），默认为0
    :return: 如果token过期，返回True；否则返回False
    """
    try:
        # 解析token
        payload = jwt.decode(token, public_systems['SECRET_KEY'], algorithms=public_systems['ALGORITHM'], leeway=leeway)
        # 如果解析成功且没有抛出异常，说明token没有过期

        # 检查Redis中的token是否被标记为无效
        if is_in_blacklist(token):
            remove_from_blacklist(token)
            return True

        return False
    except jwt.ExpiredSignatureError:
        # 如果抛出ExpiredSignatureError异常，说明token已经过期
        return True
    except Exception as e:
        # 如果抛出其他异常，可能是token无效或签名不正确等其他原因
        print(f"An error occurred while validating the token: {e}")
        return True


def execute_query(query, params=None, fetchType='one', insertMany=None):
    """
    执行SQL查询并返回结果。
    :param query: sql语句
    :param params: sql数据
    :param fetchType: 查询格式
    :param insertMany: 插入集合，None为一条数据，many为多条数据集合
    """
    try:
        cnx = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = cnx.cursor(dictionary=True)

        if insertMany == 'many':
            cursor.executemany(query, params)
        else:
            cursor.execute(query, params)

        if 'SELECT' in query.upper():
            if fetchType == 'all':
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result, None
        else:
            cnx.commit()
            # if 'INSERT' in query.upper():
            #     return cursor.lastrowid, None

            return True, None
    except Error as err:
        print(f"Error: {err}")
        return None, jsonify({'success': 0, 'msg': '数据库错误', 'error': str(err)}), 500
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()


# 分页
def paginatorData(data):

    try:
        cnx = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = cnx.cursor(dictionary=True)

        for item in data:
            if item['sel'] == 'totals':
                cursor.execute(item['statement'], item['data'])
                result_total = cursor.fetchone()
            if item['sel'] == 'page':
                cursor.execute(item['statement'], item['data'])
                result_page = cursor.fetchall()

        # 返回数组数据
        query_data = {'totals': result_total['total_records'], 'all_data': result_page}

        return query_data, None
    except Error as err:
        print(f"Error: {err}")
        return None, jsonify({'success': 0, 'msg': '数据库错误', 'error': str(err)}), 500
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()


# 生成token
def create_token(user_data):
    payload = {
        'userId': user_data['id'],
        'username': user_data['name'],
        'telephone': user_data['telephone'],
        'is_visitor': user_data['is_visitor'],
        'exp': datetime.utcnow() + timedelta(days=30)  # 设置token的过期时间 minutes/hours/days
    }
    token = jwt.encode(payload, public_systems['SECRET_KEY'], algorithm=public_systems['ALGORITHM'])

    return token
