import re

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from user.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        user_id = request.session.get('user_id')

        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
        #登陆校验
        path = request.path

        not_need_check = ['/user/login/']

        for check_path in not_need_check:
            if re.match(check_path, path):
                # 当前路径为不需要做登陆校验的路由
                return None


        if not user_id:
           return HttpResponseRedirect(reverse('user:login'))