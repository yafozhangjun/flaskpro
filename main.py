from alarm import *
from auth_group_list import *
from auth_rule_list import *
from dictionary import *
from logins import *
from flask import Flask, send_from_directory


#app = Flask(__name__)
app = Flask(__name__, static_folder='dist', static_url_path='')
@app.route('/')
def serve_vue_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dls_integration:fCgL#3SeT@8.140.198.63:3306/dls_integration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# 注册蓝图（blueprints），这些蓝图在其他文件中定义
# 登录
app.register_blueprint(login)
app.register_blueprint(register)

# 报警
app.register_blueprint(alarm)
# 用户信息


# 上传下载
# app.register_blueprint(upload)
# app.register_blueprint(images)

# 四位随机验证码
# app.register_blueprint(send_email_code)
# app.register_blueprint(send_sms_code)

app.register_blueprint(authGroup)


# 用户路由
app.register_blueprint(authRule)
app.register_blueprint(authRuleList)
app.register_blueprint(addAuthRule)
app.register_blueprint(saveAuthRule)
app.register_blueprint(delAuthRule)
app.register_blueprint(userList)
app.register_blueprint(addUser)
app.register_blueprint(saveUser)
app.register_blueprint(delUser)
app.register_blueprint(getMenuList)

# 字典
app.register_blueprint(dictionarys)
app.register_blueprint(dicList)
app.register_blueprint(addDic)
app.register_blueprint(saveDic)
app.register_blueprint(delDic)
app.register_blueprint(editPassword)
app.register_blueprint(operationLog)
app.register_blueprint(addProjectGroup)




# Swagger UI配置
"""
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # 指向Swagger的json文件

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My Flask API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/swagger.json')
def swagger_json():
    return {
        "swagger": "2.0",
        "info": {
            "title": "My API",
            "version": "1.0.0"
        },
        "paths": {
            "/": {
                "get": {
                    "description": "Root endpoint",
                    "responses": {
                        "200": {
                            "description": "A successful response"
                        }
                    }
                }
            }
        }
    }
##
"""
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
