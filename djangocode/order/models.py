from django.db import models

# Create your models here.
from App.models import UserInfo


class OrderInfo(models.Model):
    ordernumber=models.CharField(max_length=200,unique=True)
    # 订单号
    odata=models.DateTimeField(auto_now=True)
    # 订单生成时间
    oIsPay=models.BooleanField(default=False)
    # 是否支付完成（ ture 表示支付完成）
    ototal=models.DecimalField(max_digits=8,decimal_places=2)
    # 总价 整数位6位   小数位2位
    oaddress = models.CharField(max_length=200,default='beijing')
    ouser=models.ForeignKey(UserInfo,on_delete=models.CASCADE,db_column='ouser',related_name='orderinfo')

    class Meta:
        db_table='OrderInfo'








