import redis
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# SQL Server 数据库连接参数
server = '8.140.198.63:3306'
database = 'dls_integration'
username = 'dls_integration'
password = 'fCgL#3SeT'

# 创建数据库连接字符串，指定驱动程序名称
# 下面这个名称 'SQL Server' 可能需要根据你安装的驱动程序具体名称来调整

DATABASE_CONFIG = f'DRIVER={{MySQL ODBC 8.0 ANSI Driver}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
