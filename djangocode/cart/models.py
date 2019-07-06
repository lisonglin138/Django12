from django.db import models

# Create your models here.
from App.models import UserInfo
from goods.models import GoodsInfo


class CartInfo(models.Model):
    user= models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='user',related_name='ucartinfo')
    # 外键到用户
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE,db_column='goods',related_name='gcartinfo')
    # 外键商品
    count = models.IntegerField(default=1)
    # 记录用户买了多少个单位的商品
    c_is_select = models.BooleanField(default='1')
    # 购物车中选中的商品，默认为选中，0为不勾选，
    class Meta:
        db_table='cartinfo'

    def __str__(self):
        return self.user.uname + '购物车'
















