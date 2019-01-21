from django import forms
from article import models


class Form(forms.Form):

    title = forms.CharField(max_length=20,
                               min_length=1,
                               required=True,
                               error_messages = {
                                   'required':'标题字段必填',
                                   'min_length':'不能小于1字符',
                                   'max_length':'不能超过20字符'
                               })
    content = forms.CharField(required=True,
                            error_messages = {
                                'required': '内容必填'
                            })



