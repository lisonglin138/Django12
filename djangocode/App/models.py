from datetime import datetime

from django.db import models
import email
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20,unique=True)
    upassword_has=models.CharField(max_length=40)
    uemail=models.CharField(max_length=128,null=True)
    # 用户邮箱
    isactive=models.BooleanField(default=False)
    # 是否进行了邮箱激活

    isban =models.BooleanField(default=True)
    # 禁止登陆
    isdelete=models.BooleanField(default=False)
    # 逻辑删除




    uaddress=models.CharField(max_length=128,null=True)
    # 用户地址
    uyoubian=models.CharField(max_length=6,null=True)
    # 用户邮编
    uphone=models.CharField(max_length=11,default='18330066061')

    utimeCreate = models.DateTimeField(default=datetime.now())
    # 创建时间

    def __str__(self):
        return self.uname
    class Meta:
        db_table='user'

class Address(models.Model):
    aname = models.CharField(max_length=20, unique=True)
    # 地址名称
    ads = models.CharField(max_length=128, null=True)
    # 具体的地址
    aphone = models.CharField(max_length=11, default='18330066061')
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE,db_column='uid',related_name='address')
    class Meta:
        db_table='Address'



# 创建横向模板数据库
class hCategory(models.Model):

    hname=models.CharField(max_length=20,unique=True)
    hparentid=models.IntegerField(default=0)
    hclasspath=models.CharField(max_length=128,null=True)
    class Meta:
        db_table='hCategory'


# 创建纵向模板数据库
class zCategory(models.Model):
    zname = models.CharField(max_length=20, unique=True)
    zparentid = models.IntegerField(default=0)
    zclasspath = models.CharField(max_length=128, null=True)
    class Meta:
        db_table = 'zCategory'
























