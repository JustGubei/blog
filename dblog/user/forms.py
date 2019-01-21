"""__author__ =侯晨皓"""
from django import forms

from user.models import User


class LoginForm(forms.Form):

    username = forms.CharField(required=True)

    password = forms.CharField(required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == None:
            return self.cleaned_data

        else:
            user = User.objects.filter(username=username).first()
            if not user:
                raise forms.ValidationError({'user','该用户不存在'})

            if user.password != password:
                raise forms.ValidationError({'password','密码错误'})

            return self.cleaned_data
