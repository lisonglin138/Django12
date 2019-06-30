# Django12
 ni hao a 



用户名的验证

重复


前端通过颜色验证用户名重复



 productid = models.IntegerField(default=1)
    # 商品id
    productimg = models.CharField(max_length=255)
    # 商品图片
    productname = models.CharField(max_length=128)
    # 商品名称
    productlongname = models.CharField(max_length=255)
    # 商品长名字
    isxf = models.BooleanField(default=False)
    # 是否是爱鲜蜂推荐的
    pmdesc = models.BooleanField(default=False)
    # 是否是指定的商品
    specifics = models.CharField(max_length=64)
    # 产品描述
    price = models.FloatField(default=0)
    # 商品的价钱
    marketprice = models.FloatField(default=1)
    # 超市的价钱
    categoryid = models.IntegerField(default=1)
    # 分类id
    childcid = models.IntegerField(default=1)

    childcidname = models.CharField(max_length=128)
    # 名字
    dealerid = models.IntegerField(default=1)

    storenums = models.IntegerField(default=1)
    # 库存量
    productnum = models.IntegerField(default=1)
    # 商品的数量也可以认为是商品的编码
    class Meta:
        db_table = 'axf_goods'
