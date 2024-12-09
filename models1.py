# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from common.database_config import db


class AuthGroup(db.Model):
    __tablename__ = 'auth_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), nullable=False, unique=True)



class AuthGroupPermission(db.Model):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        db.Index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'group_id', 'permission_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    group_id = db.Column(db.ForeignKey('auth_group.id'), nullable=False)
    permission_id = db.Column(db.ForeignKey('auth_permission.id'), nullable=False, index=True)

    group = db.relationship('AuthGroup', primaryjoin='AuthGroupPermission.group_id == AuthGroup.id', backref='auth_group_permissions')
    permission = db.relationship('AuthPermission', primaryjoin='AuthGroupPermission.permission_id == AuthPermission.id', backref='auth_group_permissions')



class AuthPermission(db.Model):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        db.Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False)
    content_type_id = db.Column(db.ForeignKey('django_content_type.id'), nullable=False)
    codename = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), nullable=False)

    content_type = db.relationship('DjangoContentType', primaryjoin='AuthPermission.content_type_id == DjangoContentType.id', backref='auth_permissions')



class AuthUser(db.Model):
    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Unicode(128, 'Chinese_PRC_CI_AS'), nullable=False)
    last_login = db.Column(db.DateTime)
    is_superuser = db.Column(db.Integer, nullable=False)
    username = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), nullable=False, unique=True)
    first_name = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), nullable=False)
    last_name = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), nullable=False)
    email = db.Column(db.Unicode(254, 'Chinese_PRC_CI_AS'), nullable=False)
    is_staff = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Integer, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)



class AuthUserGroup(db.Model):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        db.Index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'user_id', 'group_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.ForeignKey('auth_user.id'), nullable=False)
    group_id = db.Column(db.ForeignKey('auth_group.id'), nullable=False, index=True)

    group = db.relationship('AuthGroup', primaryjoin='AuthUserGroup.group_id == AuthGroup.id', backref='auth_user_groups')
    user = db.relationship('AuthUser', primaryjoin='AuthUserGroup.user_id == AuthUser.id', backref='auth_user_groups')



class AuthUserUserPermission(db.Model):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        db.Index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'user_id', 'permission_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.ForeignKey('auth_user.id'), nullable=False)
    permission_id = db.Column(db.ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = db.relationship('AuthPermission', primaryjoin='AuthUserUserPermission.permission_id == AuthPermission.id', backref='auth_user_user_permissions')
    user = db.relationship('AuthUser', primaryjoin='AuthUserUserPermission.user_id == AuthUser.id', backref='auth_user_user_permissions')



class AuthtokenToken(db.Model):
    __tablename__ = 'authtoken_token'

    key = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.ForeignKey('auth_user.id'), nullable=False, unique=True)

    user = db.relationship('AuthUser', primaryjoin='AuthtokenToken.user_id == AuthUser.id', backref='authtoken_tokens')



class BasEquipmentManagement(db.Model):
    __tablename__ = 'bas_equipment_management'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, info='所属项目id')
    name = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='设备名称：1 锅炉、2 循环水泵、3 板式换热器')
    used = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='设备用途：一次、二次、补水')
    code = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='设备编号')
    model = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='设备型号')
    parameter = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='设备参数（锅炉填写额定功率；水泵填写流量、扬程、功率；换热器填写换热量、换热面积。）')
    address = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='所在位置')
    date = db.Column(db.Date, info='投产日期')
    useful = db.Column(db.Integer, info='使用年限（根据出厂日期或者投产日期自动计算）')
    manufacturer = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='生产厂商')
    supplier = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='供货厂商')
    state = db.Column(db.Integer, info='设备状态（1 完好、2 闲置、3 报废）')
    isdue = db.Column(db.Integer, info='是否需要年检（1 是，0 否）')
    note = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='备注')
    userId = db.Column(db.Integer, info='操作用户id')
    addTime = db.Column(db.DateTime, info='添加时间')
    updateTime = db.Column(db.DateTime, info='更新时间')
    status = db.Column(db.Integer, info='状态：1 正常，0 删除或禁用')
    qrcode = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='二维码地址')



class BasInspectionTeam(db.Model):
    __tablename__ = 'bas_inspection_team'

    id = db.Column(db.BigInteger, primary_key=True)
    team = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='班组名称')
    code = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), info='班组编码')
    personnelIds = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='人员id')
    type = db.Column(db.Integer, info='类别：1 巡检，2 维修')
    userId = db.Column(db.Integer, info='创建人id')
    addTime = db.Column(db.DateTime, info='创建时间')



class BasPipenetwork(db.Model):
    __tablename__ = 'bas_pipenetwork'

    id = db.Column(db.Integer, primary_key=True)
    pipe_name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='管网名称')
    pipe_type = db.Column(db.Integer, info='管网类型')
    pipe_year = db.Column(db.Integer, info='敷设年代')
    pipe_mode = db.Column(db.Integer, info='敷设方式')
    pipe_diameter = db.Column(db.Integer, info='管径')
    pipe_length = db.Column(db.Float(53), info='管线长度')
    pipe_map = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='管线经纬度')
    project_id = db.Column(db.Integer, info='管线连接项目')
    remark = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='备注')
    pipe_image = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='管网图片')



class BasProjectManagement(db.Model):
    __tablename__ = 'bas_project_management'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='项目名称')
    code = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='项目编码')
    type = db.Column(db.Integer, info='项目类型：1 热源站、2 隔压站、3 换热站、4 泵站')
    leader = db.Column(db.Unicode(10, 'Chinese_PRC_CI_AS'), info='负责人')
    phone = db.Column(db.Unicode(15, 'Chinese_PRC_CI_AS'), info='电话')
    address = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='地址')
    userId = db.Column(db.Integer, info='操作用户id')
    addTime = db.Column(db.DateTime, info='添加时间')
    updateTime = db.Column(db.DateTime, info='修改时间')
    heatArea = db.Column(db.Float(53), info='供热面积')
    floorage = db.Column(db.Float(53), info='建筑面积')
    status = db.Column(db.Integer, info='状态：1 正常，0 删除或禁用')
    heatType = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='建筑类型')
    heatYear = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='建筑年代')
    xymap = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='经纬度')
    filePath = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), info='文件路径')
    note = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='备注')
    is_station = db.Column(db.Integer, info='0不关联实时监控1关联实时监控')
    station_id = db.Column(db.Integer, info='站ID')



class BasStation(db.Model):
    __tablename__ = 'bas_station'

    id = db.Column(db.BigInteger, primary_key=True)
    station_id = db.Column(db.Integer, info='站ID')
    station_name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='站名称')



class BasTeamWorker(db.Model):
    __tablename__ = 'bas_team_workers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='姓名')
    telephone = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='手机号')
    __department = db.Column('\r\ndepartment', db.Unicode(50, 'Chinese_PRC_CI_AS'), info='部门')
    position = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='职位')
    state = db.Column(db.Integer, info='状态：0 禁用，1 启用')
    operator = db.Column(db.Integer, info='操作人')
    add_time = db.Column(db.DateTime, info='添加时间')



class CalFaultinfo(db.Model):
    __tablename__ = 'cal_faultinfo'

    id = db.Column(db.BigInteger, primary_key=True)
    faultType = db.Column(db.Unicode(20, 'Chinese_PRC_CI_AS'), info='故障类型')
    faultAddress = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='故障位置/形式')
    faultDiameter = db.Column(db.Unicode(20, 'Chinese_PRC_CI_AS'), info='故障管径')
    influenceArea = db.Column(db.Float(53), info='影响范围')
    occurdateTime = db.Column(db.DateTime, info='发生时间')
    predictrepairTime = db.Column(db.DateTime, info='预计修复时间')
    status = db.Column(db.Integer, info='故障状态')
    addPersons = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='上报人员')
    repairTime = db.Column(db.DateTime, info='修复时间')
    isStopWarming = db.Column(db.Integer, info='是否停暖0停暖，1限暖 2 无影响')
    seriousType = db.Column(db.Integer, info='严重程度 0：不严重 1：一般 2：严重')
    illegalType = db.Column(db.Integer, info='违规情况 0：无 1：瞒报故障 2：迟报故障')
    mapX = db.Column(db.Float(53), info='经度')
    mapY = db.Column(db.Float(53), info='纬度')
    filePath = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='图片上传')



class DatInspectionItem(db.Model):
    __tablename__ = 'dat_inspection_items'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False, info='巡检项目名称')
    text = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='巡检内容')
    filePath = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='附件')
    userId = db.Column(db.Integer, info='添加人员id')
    addTime = db.Column(db.DateTime, info='添加时间')



class DatInspectionPlan(db.Model):
    __tablename__ = 'dat_inspection_plan'

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, info='所属项目id，可多选')
    planName = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False, info='计划名称')
    teamId = db.Column(db.Integer, info='巡检班组id')
    personnelIds = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='巡检人员id（可多选）')
    cycleCount = db.Column(db.Integer, info='循环周期次数')
    cycleDate = db.Column(db.Unicode(10, 'Chinese_PRC_CI_AS'), info='循环周期日期（小时，天，周，月，季度，年）')
    loopMode = db.Column(db.Integer, info='循环方式：1 单次， 2 多次')
    startTime = db.Column(db.DateTime, info='开始时间')
    endTime = db.Column(db.DateTime, info='截至时间')
    planDescription = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='计划描述')
    itemsId = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='巡检标准id（可多选）')
    state = db.Column(db.Integer, info='状态：0 禁用，1 启用，2已结束')
    isTimeOut = db.Column(db.Integer, info='超时：1 是，0 否')
    filePath = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='附件')
    userId = db.Column(db.Integer, info='添加人id')
    addTime = db.Column(db.DateTime, info='添加时间')
    updateTime = db.Column(db.DateTime, info='修改时间')



class DatInspectionPlanReport(db.Model):
    __tablename__ = 'dat_inspection_plan_report'

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, info='所属项目id，可多选')
    planId = db.Column(db.Integer, nullable=False, info='计划id')
    teamId = db.Column(db.Integer, info='巡检班组id')
    personnelIds = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='巡检人员id（可多选）')
    content = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='巡检内容')
    filePath = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='附件')
    itemsId = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='巡检标准id（可多选）')
    userId = db.Column(db.Integer, info='添加人id')
    addTime = db.Column(db.DateTime, info='添加时间')



class DatMalfunctionBasicInformation(db.Model):
    __tablename__ = 'dat_malfunction_basic_information'

    pid = db.Column(db.Integer, nullable=False, info='项目名称--换热站名称')
    equipmentId = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='设备id')
    Faultcategory = db.Column(db.Integer, info='故障类别--自己维护字典')
    deviceNumber = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), info='设备型号')
    Voicerepair = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='语音报修')
    Repairman = db.Column(db.Unicode(20, 'Chinese_PRC_CI_AS'), info='报修人（自动识别）')
    Contactnumber = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='联系电话（自动识别）')
    Occurrencetime = db.Column(db.Date, info='发生时间 （默认报修时间，也可修改）')
    Devicelocation = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), info='设备位置（自动定位）--获取站点位置--位置描述')
    Degreeofurgency = db.Column(db.Integer, info='紧急程度（特急、紧急、不紧急）--自己维护字典--加颜色')
    Faultdescription = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='故障描述')
    Faultpicture = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='故障描述图片--图片路径')
    Auditor = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), info='审核人（默认审核流程，后台修改）')
    State = db.Column(db.Integer, info='状态列-状态（待派单、维修中、驳回、无法维修、暂存、完成）')
    number = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), primary_key=True, nullable=False, info='工单号')
    Maintenanceperson = db.Column(db.Unicode(30, 'Chinese_PRC_CI_AS'), info='维修人')
    Auditopinion = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='审核意见')
    Troubleshootingphoto = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='故障处理照片')
    addTime = db.Column(db.DateTime, info='添加时间')
    updateTime = db.Column(db.DateTime, info='修改时间')
    id = db.Column(db.Integer, primary_key=True, nullable=False)



class DatNetValue(db.Model):
    __tablename__ = 'dat_net_value'

    ID = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue(), info='id')
    ValueGroup = db.Column(db.String(255, 'Chinese_PRC_CI_AS'), info='变量分组')
    ValueName = db.Column(db.String(255, 'Chinese_PRC_CI_AS'), info='变量名')
    ValueAddress = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), info='变量地址')
    ValueType = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), info='变量类型')
    ReadWrite = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), info='读写类型')
    ValuePrice = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), info='变量值')
    TimeStamp = db.Column(db.String(255, 'Chinese_PRC_CI_AS'), info='时间戳')



t_devices = db.Table(
    'devices',
    db.Column('id', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('pid', db.Integer)
)



class DjangoAdminLog(db.Model):
    __tablename__ = 'django_admin_log'

    id = db.Column(db.Integer, primary_key=True)
    action_time = db.Column(db.DateTime, nullable=False)
    object_id = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='记录变更实例的id')
    object_repr = db.Column(db.Unicode(200, 'Chinese_PRC_CI_AS'), nullable=False, info='实例的展示名称')
    action_flag = db.Column(db.SmallInteger, nullable=False, info='操作标记')
    change_message = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), nullable=False, info='记录的消息')
    content_type_id = db.Column(db.ForeignKey('django_content_type.id'), index=True, info='要保存内容的类型')
    user_id = db.Column(db.ForeignKey('auth_user.id'), nullable=False, index=True, info='当前用户id')

    content_type = db.relationship('DjangoContentType', primaryjoin='DjangoAdminLog.content_type_id == DjangoContentType.id', backref='django_admin_logs')
    user = db.relationship('AuthUser', primaryjoin='DjangoAdminLog.user_id == AuthUser.id', backref='django_admin_logs')



class DjangoApschedulerDjangojob(db.Model):
    __tablename__ = 'django_apscheduler_djangojob'

    id = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), primary_key=True)
    next_run_time = db.Column(db.DateTime, index=True)
    job_state = db.Column(db.LargeBinary, nullable=False)



class DjangoApschedulerDjangojobexecution(db.Model):
    __tablename__ = 'django_apscheduler_djangojobexecution'
    __table_args__ = (
        db.Index('unique_job_executions', 'job_id', 'run_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    status = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), nullable=False)
    run_time = db.Column(db.DateTime, nullable=False, index=True)
    duration = db.Column(db.Numeric(15, 2))
    finished = db.Column(db.Numeric(15, 2))
    exception = db.Column(db.Unicode(1000, 'Chinese_PRC_CI_AS'))
    traceback = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'))
    job_id = db.Column(db.ForeignKey('django_apscheduler_djangojob.id'), nullable=False)

    job = db.relationship('DjangoApschedulerDjangojob', primaryjoin='DjangoApschedulerDjangojobexecution.job_id == DjangoApschedulerDjangojob.id', backref='django_apscheduler_djangojobexecutions')



class DjangoContentType(db.Model):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        db.Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model'),
    )

    id = db.Column(db.Integer, primary_key=True)
    app_label = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), nullable=False)
    model = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), nullable=False)



class DjangoMigration(db.Model):
    __tablename__ = 'django_migrations'

    id = db.Column(db.BigInteger, primary_key=True)
    app = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False)
    name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False)
    applied = db.Column(db.DateTime, nullable=False)



class DjangoSession(db.Model):
    __tablename__ = 'django_session'

    session_key = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), primary_key=True)
    session_data = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), nullable=False)
    expire_date = db.Column(db.DateTime, nullable=False, index=True)



class FeeCorrectParam(db.Model):
    __tablename__ = 'fee_correct_param'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    energy_info_id = db.Column(db.Integer, info='采暖季id')
    temp_param = db.Column(db.Float(24), info='温度系数')



t_fee_params = db.Table(
    'fee_params',
    db.Column('pid', db.Unicode(255, 'Chinese_PRC_CI_AS'), info='项目编码'),
    db.Column('date', db.DateTime, info='日期'),
    db.Column('that_day_param', db.Float(24), info='系数1'),
    db.Column('clu_day_param', db.Float(24), info='系数2'),
    db.Column('temp_avg', db.Float(24), info='平均温度'),
    db.Column('temp_max', db.Float(24), info='最高温度'),
    db.Column('temp_min', db.Float(24), info='最低温度'),
    db.Column('weather', db.Unicode(255, 'Chinese_PRC_CI_AS'), info='气象'),
    db.Column('ec_gas', db.Float(24), info='实际能耗'),
    db.Column('yc_gas', db.Float(24), info='预测能耗'),
    db.Column('yc_heat', db.Float(24), info='预测热耗')
)



class FeeStation(db.Model):
    __tablename__ = 'fee_station'

    id = db.Column(db.BigInteger, primary_key=True)
    station_id = db.Column(db.Integer, info='站ID')
    station_name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='站名称')
    sj = db.Column(db.DateTime, info='时间')
    temp_min = db.Column(db.Float(53), info='室外温度最低')
    temp_max = db.Column(db.Float(53), info='室外温度最高')
    area = db.Column(db.Float(53), info='面积')
    area_zb = db.Column(db.Float(53), info='热指标')



class FeeTemp(db.Model):
    __tablename__ = 'fee_temp'

    id = db.Column(db.BigInteger, primary_key=True)
    count_num = db.Column(db.Float(53), info='度日数/天')
    sj = db.Column(db.DateTime, info='时间')
    temp = db.Column(db.Float(53), info='当天平均室外温度')



class FeeTemperature(db.Model):
    __tablename__ = 'fee_temperature'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    date = db.Column(db.DateTime, info='日期')
    week = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='星期')
    weather = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='天气')
    temp = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='温度')
    temp_max = db.Column(db.Float(24))
    temp_min = db.Column(db.Float(24))
    temp_avg = db.Column(db.Float(24))



class Hjctrl(db.Model):
    __tablename__ = 'hjctrl'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Integer)
    jy = db.Column(db.Float(24))
    ew = db.Column(db.Float(24))
    station_id = db.Column(db.Float(24))



class StaEnergyConsume(db.Model):
    __tablename__ = 'sta_energy_consume'

    id = db.Column(db.Integer, primary_key=True)
    energy_info_id = db.Column(db.Integer, nullable=False, info='供暖期信息编号')
    pid = db.Column(db.Integer, nullable=False, info='项目编码')
    ec_gas = db.Column(db.Float(53), info='气耗量')
    ec_coal = db.Column(db.Float(53), info='煤耗量')
    ec_weather = db.Column(db.Float(53), info='水耗量')
    ec_electricity = db.Column(db.Float(53), info='电耗量')
    in_temperature = db.Column(db.Float(53), info='室内平均温度')
    out_temperature = db.Column(db.Float(53), info='室外平均温度')
    reportTime = db.Column(db.DateTime, info='数据日期')
    reportUser = db.Column(db.Integer, info='上报人')
    addTime = db.Column(db.DateTime, info='上报日期')
    updateTime = db.Column(db.DateTime, info='修改日期')



class StaEnergyInfo(db.Model):
    __tablename__ = 'sta_energy_info'

    id = db.Column(db.BigInteger, primary_key=True)
    year = db.Column(db.Unicode(10, 'Chinese_PRC_CI_AS'), info='供暖周期')
    heatDays = db.Column(db.Integer, info='实际供暖天数')
    heatPrice = db.Column(db.Float(53), info='当前供暖期热单价')
    electricPrice = db.Column(db.Float(53), info='当前供暖期电单价')
    waterPrice = db.Column(db.Float(53), info='当前供暖期水单价')
    gasPrice = db.Column(db.Float(53), info='当前供暖期气单价')
    userId = db.Column(db.Integer, info='操作人id')
    addTime = db.Column(db.DateTime, info='添加日期')
    status = db.Column(db.Integer, info='状态：1 正常，0 删除或禁用')
    startTime = db.Column(db.Date, info='供暖开始日期')
    endTime = db.Column(db.Date, info='供暖结束日期')



class SubAlarm(db.Model):
    __tablename__ = 'sub_alarm'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    station_id = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='换热站id')
    alarmName = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='报警名称')
    alarmLabel = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='报警文本')
    alarmText = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='报警提示')
    alarmType = db.Column(db.Integer, info='报警类型：1上下限报警2.故障报警')
    alarmUp = db.Column(db.Float(53), info='报警上限值')
    alarmDown = db.Column(db.Float(53), info='报警下限值')
    alarmNum = db.Column(db.Float(53), info='报警当前值')
    alarmSwitch = db.Column(db.Integer, info='报警开关')
    alarmTime = db.Column(db.Integer, info='报警时限')
    alarmLevel = db.Column(db.Integer, info='报警级别')
    alarmState = db.Column(db.Integer, info='报警状态0未处理，1已处理，2超时...')
    isOut = db.Column(db.Integer, info='是否超出上下限')
    isRead = db.Column(db.Integer, info='是否已读0未读，1已读')
    userId = db.Column(db.Integer, info='报警确认人')
    confirmTime = db.Column(db.DateTime, info='报警确认时间')
    lastTime = db.Column(db.DateTime, info='报警最后时间')
    remark = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='备注报告说明')



class SubAlarmHistory(db.Model):
    __tablename__ = 'sub_alarm_history'

    id = db.Column(db.BigInteger, primary_key=True)
    alarm_id = db.Column(db.BigInteger)
    station_id = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='换热站id')
    alarmName = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='报警名称')
    alarmLabel = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='报警文本')
    alarmText = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='报警提示')
    alarmType = db.Column(db.Integer, info='报警类型：1上下限报警2.故障报警')
    alarmUp = db.Column(db.Float(53), info='报警上限值')
    alarmDown = db.Column(db.Float(53), info='报警下限值')
    alarmNum = db.Column(db.Float(53), info='报警当前值')
    alarmSwitch = db.Column(db.Integer, info='报警开关')
    alarmTime = db.Column(db.Integer, info='报警时限')
    alarmLevel = db.Column(db.Integer, info='报警级别')
    alarmState = db.Column(db.Integer, info='报警状态0未处理，1已处理，2超时...')
    isOut = db.Column(db.Integer, info='是否超出上下限')
    isRead = db.Column(db.Integer, info='是否已读0未读，1已读')
    userId = db.Column(db.Integer, info='报警确认人')
    confirmTime = db.Column(db.DateTime, info='报警确认时间')
    lastTime = db.Column(db.DateTime, info='报警最后时间')
    remark = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='备注报告说明')



class SubAlarmTemp(db.Model):
    __tablename__ = 'sub_alarm_temp'

    id = db.Column(db.BigInteger, primary_key=True)
    station_id = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='换热站id')
    alarmName = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='报警名称')
    alarmType = db.Column(db.Integer, info='报警类型：1上下限报警2.故障报警')
    alarmUp = db.Column(db.Float(53), info='报警上限值')
    alarmDown = db.Column(db.Float(53), info='报警下限值')
    alarmNum = db.Column(db.Float(53), info='报警当前值')
    alarmSwitch = db.Column(db.Integer, info='报警开关')
    alarmTime = db.Column(db.Integer, info='报警时限')
    alarmLevel = db.Column(db.Integer, info='报警级别')
    alarmState = db.Column(db.Integer, info='报警状态0未处理，1已处理，2超时...')
    isOut = db.Column(db.Integer, info='是否超出上下限')
    isRead = db.Column(db.Integer, info='是否已读0未读，1已读')
    userId = db.Column(db.Integer, info='报警确认人')
    confirmTime = db.Column(db.DateTime, info='报警确认时间')
    lastTime = db.Column(db.DateTime, info='报警最后时间')
    remark = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='备注报告说明')



class SubDictionary(db.Model):
    __tablename__ = 'sub_dictionary'

    id = db.Column(db.BigInteger, primary_key=True)
    variable = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='变量名')
    variable_name = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='变量名称')
    alarm_type = db.Column(db.Integer, info='1上下限2故障')



class SubHeatingCommunity(db.Model):
    __tablename__ = 'sub_heating_community'

    community_id = db.Column(db.Integer, primary_key=True, info='用热组织id')
    pid = db.Column(db.Integer, nullable=False, info='项目id')
    parent_id = db.Column(db.Integer, nullable=False, info='父id')
    community_name = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='用热组织名称')
    community_area = db.Column(db.Float(53), info='用热组织面积')
    community_type = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='用热组织类型')
    add_time = db.Column(db.DateTime, info='添加时间')



class SubHeatingUser(db.Model):
    __tablename__ = 'sub_heating_users'

    heating_user_id = db.Column(db.Integer, primary_key=True, info='热用户id')
    community_id = db.Column(db.Integer, nullable=False, info='用热组织id')
    heating_user_name = db.Column(db.Unicode(20, 'Chinese_PRC_CI_AS'), info='热用户名称')
    floor_number = db.Column(db.Integer, nullable=False, info='楼层号')
    heating_user_area = db.Column(db.Float(53), info='热用户面积')
    heating_user_phone = db.Column(db.Unicode(20, 'Chinese_PRC_CI_AS'), info='热用户联系方式')
    heating_user_temp = db.Column(db.Float(53), info='热用户室内温度')
    add_time = db.Column(db.DateTime, info='添加时间')



class SubStation(db.Model):
    __tablename__ = 'sub_station'

    id = db.Column(db.BigInteger, primary_key=True)
    station_name = db.Column(db.Unicode(30, 'Chinese_PRC_CI_AS'), nullable=False, info='站名称')
    station_id = db.Column(db.Integer, nullable=False, info='站ID')
    sj = db.Column(db.DateTime, nullable=False, info='时间')
    ST_1 = db.Column(db.Numeric(10, 2), info='一次供温')
    RT_1 = db.Column(db.Numeric(10, 2), info='一次回温')
    SP_1 = db.Column(db.Numeric(10, 2), info='一次供压')
    RP_1 = db.Column(db.Numeric(10, 2), info='一次回压')
    ST_2 = db.Column(db.Numeric(10, 2), info='二次供温')
    RT_2 = db.Column(db.Numeric(10, 2), info='二次回温')
    SP_2 = db.Column(db.Numeric(10, 2), info='二次供压')
    RP_2 = db.Column(db.Numeric(10, 2), info='二次回压')
    CPF_1 = db.Column(db.Numeric(10, 2), info='一号循环泵频率')
    CPErr_1 = db.Column(db.Numeric(10, 2), info='一号循环泵故障')
    CP_1_State = db.Column(db.Numeric(10, 2), info='一号循环泵运行状态')
    CPF_2 = db.Column(db.Numeric(10, 2), info='二号循环泵频率')
    CPErr_2 = db.Column(db.Numeric(10, 2), info='二号循环泵故障')
    CP_2_State = db.Column(db.Numeric(10, 2), info='二号循环泵运行状态')
    CPF_3 = db.Column(db.Numeric(10, 2), info='三号循环泵频率')
    CPErr_3 = db.Column(db.Numeric(10, 0), info='三号循环泵故障')
    CP_3_State = db.Column(db.Numeric(10, 2), info='三号循环泵运行状态')
    MWPF_1 = db.Column(db.Numeric(10, 2), info='一号补水泵频率')
    MWPErr_1 = db.Column(db.Numeric(10, 2), info='一号补水泵故障')
    MWP_1_State = db.Column(db.Numeric(10, 2), info='一号补水泵运行状态')
    MWPF_2 = db.Column(db.Numeric(10, 2), info='二号补水泵频率')
    MWPErr_2 = db.Column(db.Numeric(10, 2), info='二号补水泵故障')
    MWP_2_State = db.Column(db.Integer, info='二号补水泵运行状态')
    RVRS = db.Column(db.Numeric(10, 2), info='泄压阀状态')
    Water_M = db.Column(db.Float(53), info='漏水报警信号')
    tjfGd = db.Column(db.Numeric(10, 2), info='调节阀开度')
    tjfFk = db.Column(db.Numeric(10, 2), info='调节阀反馈')
    tjfFs = db.Column(db.Numeric(10, 2), info='调节阀方式')
    ecycsd = db.Column(db.Numeric(10, 2), info='二次压差设定')
    echybh = db.Column(db.Numeric(10, 2), info='二次回压泵后')
    echycwqh = db.Column(db.Numeric(10, 2), info='二次回压除污器后')
    ycgyfh = db.Column(db.Numeric(10, 2), info='一次供压阀后')
    ycssll = db.Column(db.Numeric(10, 2), info='一次瞬时流量')
    ecssll = db.Column(db.Numeric(10, 2), info='二次瞬时流量')
    ycssrl = db.Column(db.Numeric(10, 2), info='一次瞬时热量')
    ecssrl = db.Column(db.Numeric(10, 2), info='二次瞬时热量')
    CW = db.Column(db.Numeric(10, 2), info='累计水量')
    CE = db.Column(db.Numeric(10, 2), info='累计电量')
    ycljrl = db.Column(db.Float(53), info='一次累计热量')
    ecljrl = db.Column(db.Float(53), info='二次累计热量')
    outTemp = db.Column(db.Numeric(10, 2), info='室外温度')
    TL = db.Column(db.Numeric(10, 2), info='液位')
    IF_MW = db.Column(db.Numeric(10, 2), info='补水瞬时流量')
    ycljll = db.Column(db.Float(53), info='一次累计流量')
    ecljll = db.Column(db.Float(53), info='二次累计流量')
    CF_MW = db.Column(db.Numeric(10, 2), info='补水累计流量')



class SubStationAlarm(db.Model):
    __tablename__ = 'sub_station_alarm'

    id = db.Column(db.BigInteger, primary_key=True)
    station_name = db.Column(db.Unicode(30, 'Chinese_PRC_CI_AS'), nullable=False, info='站名称')
    station_id = db.Column(db.Float(53), nullable=False, info='站ID')
    userId = db.Column(db.Integer, nullable=False, info='用户id')
    ST_1_U = db.Column(db.Numeric(10, 2), info='一次供温上限')
    ST_1_D = db.Column(db.Numeric(10, 2), info='一次供温下限')
    RT_1_U = db.Column(db.Numeric(10, 2), info='一次回温上限')
    RT_1_D = db.Column(db.Numeric(10, 2), info='一次回温下限')
    SP_1_U = db.Column(db.Numeric(10, 2), info='一次供压上限')
    SP_1_D = db.Column(db.Numeric(10, 2), info='一次供压下限')
    RP_1_U = db.Column(db.Numeric(10, 2), info='一次回压上限')
    RP_1_D = db.Column(db.Numeric(10, 2), info='一次回压下限')
    ST_2_U = db.Column(db.Numeric(10, 2), info='二次供温上限')
    ST_2_D = db.Column(db.Numeric(10, 2), info='二次供温下限')
    RT_2_U = db.Column(db.Numeric(10, 2), info='二次回温上限')
    RT_2_D = db.Column(db.Numeric(10, 2), info='二次回温下限')
    SP_2_U = db.Column(db.Numeric(10, 2), info='二次供压上限')
    SP_2_D = db.Column(db.Numeric(10, 2), info='二次供压下限')
    RP_2_U = db.Column(db.Numeric(10, 2), info='二次回压上限')
    RP_2_D = db.Column(db.Numeric(10, 2), info='二次回压下限')
    CPF_1_U = db.Column(db.Numeric(10, 2), info='一号循环泵频率上限')
    CPF_1_D = db.Column(db.Numeric(10, 2), info='一号循环泵频率下限')
    CPF_2_U = db.Column(db.Numeric(10, 2), info='二号循环泵频率上限')
    CPF_2_D = db.Column(db.Numeric(10, 2), info='二号循环泵频率下限')
    CPF_3_U = db.Column(db.Numeric(10, 2), info='三号循环泵频率上限')
    CPF_3_D = db.Column(db.Numeric(10, 2), info='三号循环泵频率下限')
    MWPF_1_U = db.Column(db.Numeric(10, 2), info='一号补水泵频率上限')
    MWPF_1_D = db.Column(db.Numeric(10, 2), info='一号补水泵频率下限')
    MWPF_2_U = db.Column(db.Numeric(10, 2), info='二号补水泵频率上限')
    MWPF_2_D = db.Column(db.Numeric(10, 2), info='二号补水泵频率下限')
    tjfFk_U = db.Column(db.Numeric(10, 2), info='调节阀反馈上限')
    tjfFk_D = db.Column(db.Numeric(10, 2), info='调节阀反馈下限')
    ycssll_U = db.Column(db.Numeric(10, 2), info='一次瞬时流量上限')
    ycssll_D = db.Column(db.Numeric(10, 2), info='一次瞬时流量下限')
    ecssll_U = db.Column(db.Numeric(10, 2), info='二次瞬时流量上限')
    ecssll_D = db.Column(db.Numeric(10, 2), info='二次瞬时流量下限')
    ycssrl_U = db.Column(db.Numeric(10, 2), info='一次瞬时热量上限')
    ycssrl_D = db.Column(db.Numeric(10, 2), info='一次瞬时热量下限')
    ecssrl_U = db.Column(db.Numeric(10, 2), info='二次瞬时热量上限')
    ecssrl_D = db.Column(db.Numeric(10, 2), info='二次瞬时热量下限')
    outTemp_U = db.Column(db.Numeric(10, 2), info='室外温度上限')
    outTemp_D = db.Column(db.Numeric(10, 2), info='室外温度下限')
    TL_U = db.Column(db.Numeric(10, 2), info='液位上限')
    TL_D = db.Column(db.Numeric(10, 2), info='液位下限')
    IF_MW_U = db.Column(db.Numeric(10, 2), info='补水瞬时流量')
    IF_MW_D = db.Column(db.Numeric(10, 2), info='补水瞬时流量下限')
    tjfGd = db.Column(db.Numeric(10, 2), info='调节阀开度')
    tjfFs = db.Column(db.Numeric(10, 2), info='调节阀方式')
    ecycsd = db.Column(db.Numeric(10, 2), info='二次压差设定')
    echybh = db.Column(db.Numeric(10, 2), info='二次回压泵后')
    echycwqh = db.Column(db.Numeric(10, 2), info='二次回压除污器后')
    ycgyfh = db.Column(db.Numeric(10, 2), info='一次供压阀后')
    CW = db.Column(db.Numeric(10, 2), info='累计水量')
    CE = db.Column(db.Numeric(10, 2), info='累计电量')
    ycljrl = db.Column(db.Float(53), info='一次累计热量')
    ecljrl = db.Column(db.Float(53), info='二次累计热量')
    ycljll = db.Column(db.Float(53), info='一次累计流量')
    ecljll = db.Column(db.Float(53), info='二次累计流量')
    CF_MW = db.Column(db.Numeric(10, 2), info='补水累计流量')
    CPErr_1 = db.Column(db.Numeric(10, 2), info='一号循环泵故障')
    CP_1_State = db.Column(db.Numeric(10, 2), info='一号循环泵运行状态')
    CPErr_2 = db.Column(db.Numeric(10, 2), info='二号循环泵故障')
    CP_2_State = db.Column(db.Numeric(10, 2), info='二号循环泵运行状态')
    CPErr_3 = db.Column(db.Numeric(10, 0), info='三号循环泵故障')
    CP_3_State = db.Column(db.Numeric(10, 2), info='三号循环泵运行状态')
    MWPErr_1 = db.Column(db.Numeric(10, 2), info='一号补水泵故障')
    MWP_1_State = db.Column(db.Numeric(10, 2), info='一号补水泵运行状态')
    MWPErr_2 = db.Column(db.Numeric(10, 2), info='二号补水泵故障')
    MWP_2_State = db.Column(db.Integer, info='二号补水泵运行状态')
    RVRS = db.Column(db.Numeric(10, 2), info='泄压阀状态')
    Water_M = db.Column(db.Float(53), info='漏水报警信号')



class SubStationHistory(db.Model):
    __tablename__ = 'sub_station_history'

    id = db.Column(db.BigInteger, primary_key=True)
    station_name = db.Column(db.Unicode(30, 'Chinese_PRC_CI_AS'), nullable=False, info='站名称')
    station_id = db.Column(db.Float(53), nullable=False, info='站ID')
    sj = db.Column(db.DateTime, nullable=False, info='时间')
    ST_1 = db.Column(db.Numeric(10, 2), info='一次供温')
    RT_1 = db.Column(db.Numeric(10, 2), info='一次回温')
    SP_1 = db.Column(db.Numeric(10, 2), info='一次供压')
    RP_1 = db.Column(db.Numeric(10, 2), info='一次回压')
    ST_2 = db.Column(db.Numeric(10, 2), info='二次供温')
    RT_2 = db.Column(db.Numeric(10, 2), info='二次回温')
    SP_2 = db.Column(db.Numeric(10, 2), info='二次供压')
    RP_2 = db.Column(db.Numeric(10, 2), info='二次回压')
    CPF_1 = db.Column(db.Numeric(10, 2), info='一号循环泵频率')
    CPErr_1 = db.Column(db.Numeric(10, 2), info='一号循环泵故障')
    CP_1_State = db.Column(db.Numeric(10, 2), info='一号循环泵运行状态')
    CPF_2 = db.Column(db.Numeric(10, 2), info='二号循环泵频率')
    CPErr_2 = db.Column(db.Numeric(10, 2), info='二号循环泵故障')
    CP_2_State = db.Column(db.Numeric(10, 2), info='二号循环泵运行状态')
    CPF_3 = db.Column(db.Numeric(10, 2), info='三号循环泵频率')
    CPErr_3 = db.Column(db.Numeric(10, 0), info='三号循环泵故障')
    CP_3_State = db.Column(db.Numeric(10, 2), info='三号循环泵运行状态')
    MWPF_1 = db.Column(db.Numeric(10, 2), info='一号补水泵频率')
    MWPErr_1 = db.Column(db.Numeric(10, 2), info='一号补水泵故障')
    MWP_1_State = db.Column(db.Numeric(10, 2), info='一号补水泵运行状态')
    MWPF_2 = db.Column(db.Numeric(10, 2), info='二号补水泵频率')
    MWPErr_2 = db.Column(db.Numeric(10, 2), info='二号补水泵故障')
    MWP_2_State = db.Column(db.Integer, info='二号补水泵运行状态')
    RVRS = db.Column(db.Numeric(10, 2), info='泄压阀状态')
    Water_M = db.Column(db.Float(53), info='漏水报警信号')
    tjfGd = db.Column(db.Numeric(10, 2), info='调节阀开度')
    tjfFk = db.Column(db.Numeric(10, 2), info='调节阀反馈')
    tjfFs = db.Column(db.Numeric(10, 2), info='调节阀方式')
    ecycsd = db.Column(db.Numeric(10, 2), info='二次压差设定')
    echybh = db.Column(db.Numeric(10, 2), info='二次回压泵后')
    echycwqh = db.Column(db.Numeric(10, 2), info='二次回压除污器后')
    ycgyfh = db.Column(db.Numeric(10, 2), info='一次供压阀后')
    ycssll = db.Column(db.Numeric(10, 2), info='一次瞬时流量')
    ecssll = db.Column(db.Numeric(10, 2), info='二次瞬时流量')
    ycssrl = db.Column(db.Numeric(10, 2), info='一次瞬时热量')
    ecssrl = db.Column(db.Numeric(10, 2), info='二次瞬时热量')
    CW = db.Column(db.Numeric(10, 2), info='累计水量')
    CE = db.Column(db.Numeric(10, 2), info='累计电量')
    ycljrl = db.Column(db.Float(53), info='一次累计热量')
    ecljrl = db.Column(db.Float(53), info='二次累计热量')
    outTemp = db.Column(db.Numeric(10, 2), info='室外温度')
    TL = db.Column(db.Numeric(10, 2), info='液位')
    IF_MW = db.Column(db.Numeric(10, 2), info='补水瞬时流量')
    ycljll = db.Column(db.Float(53), info='一次累计流量')
    ecljll = db.Column(db.Float(53), info='二次累计流量')
    CF_MW = db.Column(db.Numeric(10, 2), info='补水累计流量')



class SysAuthGroup(db.Model):
    __tablename__ = 'sys_auth_group'

    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='名称')
    status = db.Column(db.Integer, info='状态：为1正常，为0禁用')
    rules = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='路由表id')
    projectGroup = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='项目id')
    userId = db.Column(db.Integer, info='操作员id')
    addTime = db.Column(db.DateTime, info='添加时间')



class SysAuthRule(db.Model):
    __tablename__ = 'sys_auth_rule'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, info='父级id')
    path = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='路由访问路径')
    name = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='路由 name')
    redirect = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='重定向路径')
    component = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='视图文件路径')
    icon = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), info='菜单和面包屑对应的图标')
    title = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='路由标题 ')
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
    miniIcon = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='小程序图标')
    image = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='图标')



class SysDictionary(db.Model):
    __tablename__ = 'sys_dictionary'

    id = db.Column(db.Integer, primary_key=True, info='ID')
    pid = db.Column(db.Integer, info='父id')
    workName = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), info='名称')
    workCode = db.Column(db.Unicode(30, 'Chinese_PRC_CI_AS'), info='编码')
    note = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='备注')
    addTime = db.Column(db.DateTime, info='添加时间')
    setValue = db.Column(db.Unicode(40, 'Chinese_PRC_CI_AS'), info='隐藏值')



class SysOperationLog(db.Model):
    __tablename__ = 'sys_operation_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, info='操作用户id')
    path = db.Column(db.Unicode(150, 'Chinese_PRC_CI_AS'), info='请求路径')
    ip = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='请求ip')
    method = db.Column(db.Unicode(8, 'Chinese_PRC_CI_AS'), info='请求方式')
    code = db.Column(db.Unicode(8, 'Chinese_PRC_CI_AS'), info='响应码')
    params = db.Column(db.Unicode(collation='Chinese_PRC_CI_AS'), info='变更内容')
    add_time = db.Column(db.DateTime, info='操作时间')



class SysUser(db.Model):
    __tablename__ = 'sys_user'

    userId = db.Column(db.Integer, primary_key=True, info='用户ID')
    userName = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='用户名')
    realName = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='姓名')
    passWord = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='密码')
    roleId = db.Column(db.Integer, info='角色ID')
    telePhone = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), info='电话')
    address = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='地址')
    operatorId = db.Column(db.Integer, info='操作员id')
    addTime = db.Column(db.DateTime, info='添加时间')
    teamId = db.Column(db.Integer, info='班组（1 巡检，2 维修）')
    email = db.Column(db.Unicode(50, 'Chinese_PRC_CI_AS'), info='邮箱')
    positionId = db.Column(db.Integer, info='职位')
    state = db.Column(db.Integer, info='状态（1正常，0禁用）')



class SysUserToken(db.Model):
    __tablename__ = 'sys_user_token'

    id = db.Column(db.BigInteger, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    roleId = db.Column(db.Integer)
    token = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False)
    update_time = db.Column(db.DateTime)



class TagBasicInfo(db.Model):
    __tablename__ = 'tag_basic_info'

    TagID = db.Column(db.Integer, primary_key=True)
    TagName = db.Column(db.String(255, 'Chinese_PRC_CI_AS'))
    TagComment = db.Column(db.String(255, 'Chinese_PRC_CI_AS'))
    StructTagID = db.Column(db.Integer)
    AlarmGroupID = db.Column(db.Integer)
    TagDataType = db.Column(db.Integer)
    TagType = db.Column(db.SmallInteger)
    AccessbyOtherApp = db.Column(db.Boolean)
    WriteLength = db.Column(db.BigInteger)
    FieldValue = db.Column(db.String(255, 'Chinese_PRC_CI_AS'))
    TimeStamp = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'))
    IsWrite = db.Column(db.Integer, server_default=db.FetchedValue())
    TagGroupID = db.Column(db.Integer)



class TagBasicInfo38(db.Model):
    __tablename__ = 'tag_basic_info_38'

    TagID = db.Column(db.Integer, primary_key=True)
    TagName = db.Column(db.String(255, 'Chinese_PRC_CI_AS'))
    TagComment = db.Column(db.String(255, 'Chinese_PRC_CI_AS'))
    StructTagID = db.Column(db.Integer)
    AlarmGroupID = db.Column(db.Integer)
    TagDataType = db.Column(db.Integer)
    TagType = db.Column(db.SmallInteger)
    AccessbyOtherApp = db.Column(db.Boolean)
    WriteLength = db.Column(db.BigInteger)
    FieldValue = db.Column(db.String(255, 'Chinese_PRC_CI_AS'))
    TimeStamp = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'))



class TagCraftConfig(db.Model):
    __tablename__ = 'tag_craft_config'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue(), info='序号')
    craftName = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='工艺名称')
    craftVariable = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='工艺变量')
    tagID = db.Column(db.Integer, info='点id')
    tagName = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='点名称')
    tagValue = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='点值')
    cameraView = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='相机视角')
    cameraCrossSectionMin = db.Column(db.Float(53))
    cameraCrossSectionMax = db.Column(db.Float(53), info='相机最小截面')
    cameraPositionX = db.Column(db.Float(53), info='相机最大截面')
    cameraPositionY = db.Column(db.Float(53), info='相机位置X')
    cameraPositionZ = db.Column(db.Float(53), info='相机位置Y')
    pname = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='相机位置Z')
    pid = db.Column(db.Integer, info='项目名称')
    addTime = db.Column(db.DateTime, info='项目id')
    updateTime = db.Column(db.DateTime, info='新增时间')
    craftGroupName = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), info='更新时间')



class UtilDocument(db.Model):
    __tablename__ = 'util_document'

    id = db.Column(db.BigInteger, primary_key=True)
    uploaded_at = db.Column(db.DateTime, nullable=False)
    upload = db.Column(db.Unicode(100, 'Chinese_PRC_CI_AS'), nullable=False)
    original_name = db.Column(db.Unicode(255, 'Chinese_PRC_CI_AS'), nullable=False)
