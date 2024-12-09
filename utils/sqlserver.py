import pyodbc

# SQL Server 数据库连接参数
server = '8.140.198.63:3306'
database = 'dls_integration'
username = 'dls_integration'
password = 'fCgL#3SeT'

# 创建数据库连接字符串，指定驱动程序名称
# 下面这个名称 'SQL Server' 可能需要根据你安装的驱动程序具体名称来调整
connection_string = f'DRIVER={{MySQL ODBC 8.0 ANSI Driver}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # 尝试连接到数据库
    conn = pyodbc.connect(connection_string)
    print("连接成功！")

    # 创建游标对象
    cursor = conn.cursor()

    # SQL 语句
    sql_query = "SELECT * FROM bas_project_management"  # 替换为你要执行的SQL语句

    # 执行SQL语句
    cursor.execute(sql_query)

    # 获取查询结果
    rows = cursor.fetchall()
    return_data = []
    # 打印查询结果
    for row in rows:
        data = {
            "id": row[0],
            "station_name": row[1],
            "supplied_area": 0,
            "children": []
        }
        sql_query2 = "SELECT * FROM tag_basic_info WHERE TagGroupID = "+ row[0]  # 替换为你要执行的SQL语句
        # 执行SQL语句
        cursor.execute(sql_query2)

        # 获取查询结果
        rows_value = cursor.fetchall()
        for row_value in rows_value:
            data['children'].append(
                {
                    row_value[0]: row_value[9]
                }
            )

    # 关闭游标和连接
    cursor.close()
    conn.close()

except Exception as e:
    print(f"数据库连接或查询失败: {e}")
