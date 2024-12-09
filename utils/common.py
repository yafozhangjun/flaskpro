import json
import uuid

import numpy as np
from django.core.paginator import Paginator
from django.core import serializers
from datetime import datetime
from dateutil.relativedelta import relativedelta

from models import SysDictionary


# from Dictionary.models import SysDictionary
# from EnergyAnalysis.models import StaEnergyInfo


# # 分页
# def paginatorData(page_size, page_num, data):
#     paginator = Paginator(data, page_size)
#     page_obj = paginator.get_page(page_num)
#
#     json_data = getArrayList(page_obj)
#     return json_data
#
#
# # 转换数组
# def getArrayList(data):
#     data_obj = serializers.serialize('json', list(data))
#     json_data = json.loads(data_obj)
#     rel = []
#     for item in json_data:
#         item['fields']['id'] = item['pk']
#         rel.append(item['fields'])
#
#     return rel
#
def to_array_list(query):
    """
    将SQLAlchemy查询对象转换为列表（ArrayList）。

    :param query: SQLAlchemy查询对象
    :return: 包含查询结果的列表，每个元素是一个字典
    """
    data = query.all()
    # 使用列表推导式和make_dict方法转换查询结果
    array_list = [make_dict(record) for record in data]
    return array_list


def model_to_dict(instance):
    output = {}
    for column in instance.__table__.columns:
        output[column.name] = getattr(instance, column.name)
    return output


def make_dict(record):
    """
    将SQLAlchemy模型实例转换为字典。

    :param record: SQLAlchemy模型实例
    :return: 模型实例的字典表示
    """
    # 使用__dict__获取模型实例的所有属性和值
    # 使用items()方法将它们转换为一个字典
    # 排除掉内置的跟踪记录字段
    return {column: value for column, value in record.__dict__.items() if not column.startswith('_')}


def paginate_query(query, page, per_page):
    """
    为SQLAlchemy查询对象应用分页。

    :param query: SQLAlchemy查询对象
    :param page: 当前页码
    :param per_page: 每页显示的记录数
    :return: 分页后的查询对象
    """
    # 计算偏移量（跳过的记录数）
    offset = (page-1) * per_page
    # 应用limit和offset来获取特定页面的结果
    paginated_query = query.limit(per_page).offset(offset)
    return to_array_list(paginated_query)

# # Flask translation of Django methods
# def getProjectName(data):
#     pids = [item['pid'] for item in data]
#     print(data)
#     print(pids)
#     p_data = BasProjectManagement.query.filter(BasProjectManagement.id.in_(pids)).all()
#     p_dict = {p.id: p.name for p in p_data}
#     print(p_dict)
#     for item in data:
#         item['pname'] = p_dict.get(item['pid'], '')
#     return data

def getDictionName(data, dicStr):
    dicNameStr = dicStr + 'Name'
    dids = [item[dicStr] for item in data]
    p_data = SysDictionary.query.filter(SysDictionary.id.in_(dids)).all()
    p_dict = {p.id: p.workName for p in p_data}
    for item in data:
        if item[dicStr] is not None:
            item[dicNameStr] = p_dict.get(int(item[dicStr]), '')
        else:
            item[dicNameStr] = ""
    return data

def getDictionParam(data, dicStr):
    dicNameStr = dicStr + 'Param'
    dids = [item[dicStr] for item in data]
    p_data = SysDictionary.query.filter(SysDictionary.id.in_(dids)).all()
    p_dict = {p.id: p.setvalue for p in p_data}
    for item in data:
        item[dicNameStr] = p_dict.get(item[dicStr], '')
    return data

def getDictionId(data, dicType, dicStr, dname):
    dic_fdata = SysDictionary.query.filter_by(workName=dicType, pid=0).first()
    dic_data = SysDictionary.query.filter_by(pid=dic_fdata.id).all()
    dic_array = {dic.workName: dic.id for dic in dic_data}
    for d in data:
        d[dname] = dic_array.get(d[dicStr])
    return data

# def getBasProjectName(data, name):
#     proData = BasProjectManagement.query.all()
#     proData = to_array_list(proData)
#     pro_array = {dic['id']: dic['name'] for dic in proData}
#     for d in data:
#         d[name] = pro_array.get(d['pid'])
#     return data

# 转换时间格式
# 2023-11-26T00:00:00 转为 2023-11-26 00:00:00
def getTimeStr(date_time):
    datetime_obj = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
    formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


# 转换时间戳
def getTimeStamp(date_time, obj):
    if obj == 1:
        time = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S')
    else:
        time = datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')

    timestamp = time.timestamp()
    return timestamp


def generate_order_number():
    # 生成订单唯一编号
    # 生成 UUID
    order_uuid = uuid.uuid4()
    # 获取 UUID 的前八位
    order_prefix = str(order_uuid)[:8]
    # 拼接订单编号
    formatted_date = datetime.now().strftime("%Y%m%d%H%M%S")
    order_number = f"{formatted_date}{order_prefix}"
    return order_number


# 菜单无极限分类
def build_tree(data, p_str='pid', id_str='id', pid=0):
    resule = []
    for item in data:
        if item[p_str] == pid:
            item['children'] = build_tree(data, p_str, id_str, item[id_str])
            resule.append(item)
    return resule


def isNan(value):
    if type(value) == str:
        return False
    elif not np.isnan(float(value)):
        return True


# 计算时间
def getTimestamp(time, obj, num=1):
    if type(time) == str:
        time = datetime.strptime(time, '%Y-%m-%d').date()

    if obj == 'days':
        time_obj = (time - relativedelta(days=num)).strftime('%Y-%m-%d')
    elif obj == 'years':
        time_obj = (time - relativedelta(years=num)).strftime('%Y-%m-%d')

    return datetime.strptime(time_obj, '%Y-%m-%d')
