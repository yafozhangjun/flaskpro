# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from common.database_config import db


class CpDept(db.Model):
    __tablename__ = 'cp_dept'

    id = db.Column(db.Integer, primary_key=True, info='部门ID')
    parent_id = db.Column(db.Integer, info='父级编号')
    dept_name = db.Column(db.String(50), info='部门名称')
    leader = db.Column(db.String(50), info='负责人')
    phone = db.Column(db.String(20), info='联系方式')
    email = db.Column(db.String(50), info='邮箱')
    status = db.Column(db.Integer, info='状态(1开启,0关闭)')
    comment = db.Column(db.Text, info='备注')
    address = db.Column(db.String(255), info='详细地址')
    sort = db.Column(db.Integer, info='排序')
    create_at = db.Column(db.DateTime, info='创建时间')



class CpUser(db.Model):
    __tablename__ = 'cp_user'

    id = db.Column(db.Integer, primary_key=True, info='用户ID')
    username = db.Column(db.String(20), info='用户名')
    realname = db.Column(db.String(20), info='真实名字')
    mobile = db.Column(db.String(11), info='电话号码')
    avatar = db.Column(db.String(255), info='头像')
    comment = db.Column(db.String(255), info='备注')
    password_hash = db.Column(db.String(128), info='哈希密码')
    enable = db.Column(db.Integer, info='启用')
    dept_id = db.Column(db.Integer, info='部门id')
    create_at = db.Column(db.DateTime, info='创建时间')
    update_at = db.Column(db.DateTime, info='更新时间')



class FilePhoto(db.Model):
    __tablename__ = 'file_photo'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255))
    mime = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(30), nullable=False)
    create_at = db.Column(db.DateTime, info='创建时间')
    update_at = db.Column(db.DateTime, info='更新时间')



class LgLogging(db.Model):
    __tablename__ = 'lg_logging'

    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    uid = db.Column(db.Integer)
    url = db.Column(db.String(255))
    desc = db.Column(db.Text)
    ip = db.Column(db.String(255))
    success = db.Column(db.Integer)
    user_agent = db.Column(db.Text)
    create_at = db.Column(db.DateTime, info='创建时间')
    update_at = db.Column(db.DateTime, info='更新时间')



class RtPower(db.Model):
    __tablename__ = 'rt_power'

    id = db.Column(db.Integer, primary_key=True, info='权限编号')
    name = db.Column(db.String(255), info='权限名称')
    type = db.Column(db.SmallInteger, info='权限类型')
    code = db.Column(db.String(30), info='权限标识')
    url = db.Column(db.String(255), info='权限路径')
    open_type = db.Column(db.String(10), info='打开方式')
    parent_id = db.Column(db.Integer, index=True, info='父类编号')
    icon = db.Column(db.String(128), info='图标')
    sort = db.Column(db.Integer, info='排序')
    enable = db.Column(db.Integer, info='是否开启')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')



class RtRole(db.Model):
    __tablename__ = 'rt_role'

    id = db.Column(db.Integer, primary_key=True, info='角色ID')
    name = db.Column(db.String(255), info='角色名称')
    code = db.Column(db.String(255), info='角色标识')
    enable = db.Column(db.Integer, info='是否启用')
    comment = db.Column(db.String(255), info='备注')
    details = db.Column(db.String(255), info='详情')
    sort = db.Column(db.Integer, info='排序')
    create_time = db.Column(db.DateTime, info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')



class RtRolePower(db.Model):
    __tablename__ = 'rt_role_power'

    id = db.Column(db.Integer, primary_key=True, info='标识')
    power_id = db.Column(db.Integer, index=True, info='用户编号')
    role_id = db.Column(db.Integer, index=True, info='角色编号')



class RtUserRole(db.Model):
    __tablename__ = 'rt_user_role'

    id = db.Column(db.Integer, primary_key=True, info='标识')
    user_id = db.Column(db.Integer, index=True, info='用户编号')
    role_id = db.Column(db.Integer, index=True, info='角色编号')



class SysAuthGroup(db.Model):
    __tablename__ = 'sys_auth_group'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(100), info='名称')
    status = db.Column(db.Integer, info='状态：为1正常，为0禁用')
    rules = db.Column(db.String, info='路由表id')
    projectGroup = db.Column(db.String, info='项目id')
    userId = db.Column(db.Integer, info='操作员id')
    addTime = db.Column(db.DateTime, info='添加时间')



class SysAuthRule(db.Model):
    __tablename__ = 'sys_auth_rule'

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, info='父级id')
    path = db.Column(db.String(100), info='路由访问路径')
    name = db.Column(db.String(50), info='路由 name')
    redirect = db.Column(db.String(255), info='重定向路径')
    component = db.Column(db.String(255), info='视图文件路径')
    icon = db.Column(db.String(40), info='菜单和面包屑对应的图标')
    title = db.Column(db.String(255), info='路由标题 ')
    isLink = db.Column(db.Integer, info='路由外链时填写的访问地址')
    isHide = db.Column(db.Integer, info='是否在菜单中隐藏，1 正常，0 隐藏')
    isFull = db.Column(db.Integer, info='菜单是否全屏')
    isAffix = db.Column(db.Integer, info='菜单是否固定在标签页中')
    isKeepAlive = db.Column(db.Integer, info='前路由是否缓存')
    isAdd = db.Column(db.Integer, info='是否显示新增按钮（1 是，0 否）')
    isEdit = db.Column(db.Integer, info='是否显示修改按钮（1 是，0 否）')
    isDel = db.Column(db.Integer, info='是否显示删除按钮（1 是，0 否）')
    sort = db.Column(db.Integer, info='排序')
    miniPage = db.Column(db.Integer, info='小程序显示位于页面')
    miniIcon = db.Column(db.String(255), info='小程序图标')
    image = db.Column(db.String(255), info='图标')



class SysDictionary(db.Model):
    __tablename__ = 'sys_dictionary'

    id = db.Column(db.Integer, primary_key=True, info='ID')
    pid = db.Column(db.Integer, info='父id')
    workName = db.Column(db.String(40), info='名称')
    workCode = db.Column(db.String(30), info='编码')
    note = db.Column(db.String(255), info='备注')
    addTime = db.Column(db.DateTime, info='添加时间')
    setValue = db.Column(db.String(40), info='隐藏值')



class SysOperationLog(db.Model):
    __tablename__ = 'sys_operation_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, info='操作用户id')
    path = db.Column(db.String(150), info='请求路径')
    ip = db.Column(db.String(50), info='请求ip')
    method = db.Column(db.String(8), info='请求方式')
    code = db.Column(db.String(8), info='响应码')
    params = db.Column(db.String, info='变更内容')
    add_time = db.Column(db.DateTime, info='操作时间')



class SysUser(db.Model):
    __tablename__ = 'sys_user'

    userId = db.Column(db.Integer, primary_key=True, info='用户ID')
    userName = db.Column(db.String(100), info='用户名')
    realName = db.Column(db.String(100), info='姓名')
    passWord = db.Column(db.String(100), info='密码')
    roleId = db.Column(db.Integer, info='角色ID')
    telePhone = db.Column(db.String(100), info='电话')
    address = db.Column(db.String(255), info='地址')
    operatorId = db.Column(db.Integer, info='操作员id')
    addTime = db.Column(db.DateTime, info='添加时间')
    teamId = db.Column(db.Integer, info='班组（1 巡检，2 维修）')
    email = db.Column(db.String(50), info='邮箱')
    positionId = db.Column(db.Integer, info='职位')
    state = db.Column(db.Integer, info='状态（1正常，0禁用）')



class SysUserToken(db.Model):
    __tablename__ = 'sys_user_token'

    id = db.Column(db.BigInteger, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    roleId = db.Column(db.Integer)
    token = db.Column(db.String(255), nullable=False)
    update_time = db.Column(db.DateTime)
