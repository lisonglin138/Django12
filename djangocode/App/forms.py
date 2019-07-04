import re

from django import  forms
from django.core.exceptions import ValidationError

from App.models import UserInfo


# def check_upassword_has(value):
def check_password(value):
    if re.match(r'\d+$',value):
        raise ValidationError('密码不能是纯数字')





# 创建用户登录的表单验证
class UserInfoForm(forms.Form):
    uname = forms.CharField(label='用户名', min_length=3,max_length=30,
                            error_messages={
                                'required':'必填',
                                'min_length':'最少3位字符',
                                'max_length':'最多20位字符'
                            })
    upassword_has=forms.CharField(label='密码',validators=[check_password],min_length=6,max_length=128,widget=forms.PasswordInput(),error_messages={
        'required':'必填',
        'min_length':'最少6位字符',
        'max_length':'最多128位字符'
    })
    confirm_password = forms.CharField(label='确认密码',validators=[check_password],min_length=6,max_length=128,widget=forms.PasswordInput(),error_messages={
        'required':'必填',
        'min_length':'最少6位字符',
        'max_length':'最多128位字符'
    })
    uemail = forms.EmailField(label='邮箱',required=False,error_messages={
        'invalid':"邮箱格式无效"
    })
    uphone = forms.CharField(label='电话',min_length=11,required=False,error_messages={
        'min_length':'至少11位'
    })
    # utimeCreate=forms.DateTimeField(label='注册日期',error_messages={
    #     'invalid':"日期格式错误"
    # })

    # 验证用户名
    def clean_uname(self):
        name=self.cleaned_data.get('uname')
        res =UserInfo.objects.filter(uname=name).exists()
        if res:
            raise ValidationError('%s 用户已经存在'%name)

        else:
            return name

    #  验证单个字段
    def clean_uphone(self):
        # phone 替换成html中表示电话的那个变量
        value = self.cleaned_data.get('uphone')
        if not re.match(r'1[35678]\d{9}$',value):
            raise ValidationError('手机号码不正确，请重新填写')
        else:
            return value


        # 验证两次密码不一致
        # clean 后面带  “-”说明不是全局的是单个属性的判断
        #     不加’-‘ 说明是全局的
    def clean(self):
        password1=self.cleaned_data.get('upassword_has')
        password2=self.cleaned_data.get('confirm_password')
        print(password1,password2)
        if password1 != password2:
            raise ValidationError({'confirm_password':'两次密码不一致'})
            # raise ValidationError( '两次密码不一致')
        else:
            return self.cleaned_data


class loginForm(forms.Form):
    uname = forms.CharField(label='用户名', min_length=3, max_length=30,
                            error_messages={
                                'required': '必填',
                                'min_length': '最少3位字符',
                                'max_length': '最多20位字符'
                            })
    upassword_has = forms.CharField(label='密码', validators=[check_password], min_length=6, max_length=128,
                                    widget=forms.PasswordInput(), error_messages={
            'required': '必填',
            'min_length': '最少6位字符',
            'max_length': '最多128位字符'
        })























