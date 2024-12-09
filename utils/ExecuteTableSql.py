# import pymysql
#
#
# def ExecuteCreatTableSql(table_name, old_table):
#
#     try:
#         # 建立数据库连接
#         conn = pymysql.connect(
#             host="8.141.1.2",
#             user="wlmq",
#             password="wlmq",
#             database="tht",
#             cursorclass=pymysql.cursors.DictCursor
#         )
#
#         # 创建游标
#         with conn.cursor() as cursor:
#             Str = "CREATE TABLE " + table_name
#             Str += " LIKE " + old_table
#             print(Str)
#             cursor.execute(Str)
#             rows = cursor.fetchall()
#             new_rows = [{k.lower(): v for k, v in d.items()} for d in rows]
#
#             # 如果是插入、删除、更新语句切记要写提交命令con.commit()
#
#     finally:
#         conn.close()
#         return new_rows