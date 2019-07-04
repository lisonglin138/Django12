from django.db import models

# Create your models here.
class GoodsType(models.Model):
    #商品分类表
    title=models.CharField(max_length=128)
    gparentid=models.IntegerField(default=0)
    isdelete=models.BooleanField(default=False)
    desc = models.CharField(max_length=128,null=True)
    class Meta:
        db_table='goodstype'
    def __str__(self):
        return self.title

class GoodsInfo(models.Model):
    #  具体的商品信息
    gname=models.CharField(max_length=32,unique=True)
    gprice =models.DecimalField(max_digits=6,decimal_places=2)
    # 商品价格 小数点为2位   整数位为三位
    gpic=models.CharField(max_length=128,null=True)
    # 商品照片
    isdelete=models.BooleanField(default=False)
    gweight=models.CharField(max_length=200,default='500g')
    #  单位重量
    gsum=models.IntegerField(default=0)
    # 库存


    gdesc =models.CharField(max_length=200,null=True)
    # 简介
    gclick = models.IntegerField(default=0)
    #  点击量
    gcontent =models.CharField(max_length=200,null=True)
    # 商品详情
    # 一对多
    gtype=models.ForeignKey(GoodsType,on_delete=models.CASCADE,db_column='gtype',related_name='goodsinfo',)

    class Meta:
        db_table="GoodsInfo"
    def __str__(self):
        return self.gname










