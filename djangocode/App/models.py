from datetime import datetime

from django.db import models
import email
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20,unique=True)
    upassword_has=models.CharField(max_length=40)
    uemail=models.CharField(max_length=128,null=True)
    isban =models.BooleanField(default=True)
    isdelete=models.BooleanField(default=False)

    uaddress=models.CharField(max_length=128,null=True)
    uyoubian=models.CharField(max_length=6,null=True)
    uphone=models.CharField(max_length=11,default='18330066061')
    utimeCreate = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.uname
    class Meta:
        db_table='user'

class Address(models.Model):
    aname = models.CharField(max_length=20, unique=True)
    ads = models.CharField(max_length=128, null=True)
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
























