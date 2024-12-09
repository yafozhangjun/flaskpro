from django.db import models
from django.utils.crypto import get_random_string
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
import json
from User.models import *
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from datetime import datetime
from django.http import HttpResponse

from models import SysUserToken, SysAuthGroup, SysOperationLog


class Authtication(BaseAuthentication):
    """用户是否登录成功认证类, 如果有token代表登录成功,如果没token代表登录失败"""

    def authenticate(self, request):
        token = request._request.headers['Authorization']
        user_token = SysUserToken.objects.filter(token=token).first()
        if not user_token:
            raise exceptions.AuthenticationFailed("用户认证失败")

        # 判断项目权限
        project_auth = SysAuthGroup.objects.filter(id=user_token.roleid).get()
        request.projectgroup = project_auth.projectgroup.split(',') if project_auth.projectgroup else None

        # 记录操作日志
        url_userid = user_token.userid
        url_path = request.path
        url_ip = request.META.get('HTTP_HOST')
        # url_address = request.META.get('REMOTE_ADDR')
        url_method = request.method
        url_code = HttpResponse().status_code
        if request.method == 'POST':
            url_params = json.loads(request.body) if request.body else '{}'
        else:
            url_params = request.GET.dict()
        now_time = datetime.now()
        url_addtime = now_time.strftime('%Y-%m-%d %H:%M:%S')
        SysOperationLog.objects.create(user_id=url_userid, path=url_path, ip=url_ip, method=url_method, code=url_code, params=url_params, add_time=url_addtime)

        # 传递的这个元组就会赋值给request对象的两个属性：request.user, request.auth
        return (user_token.userid, token)

    def authenticate_header(self, request):
        pass
