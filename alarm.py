import hashlib
import json



import pyodbc
from flask import Flask, request, jsonify, Blueprint
from common.database_config import *
from common.public_method import *
from datetime import datetime
import time
alarm = Blueprint('alarm', __name__)

# 验证登录
@alarm.route('/alarm/dictionary', methods=['POST'])
def dictionary_index():
    return jsonify({'success': 1, 'msg': '登陆成功', 'data': {'list':[]}}), 200





