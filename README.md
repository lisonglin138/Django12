# Django12
 ni hao a 



�û�������֤

�ظ�


ǰ��ͨ����ɫ��֤�û����ظ�



 productid = models.IntegerField(default=1)
    # ��Ʒid
    productimg = models.CharField(max_length=255)
    # ��ƷͼƬ
    productname = models.CharField(max_length=128)
    # ��Ʒ����
    productlongname = models.CharField(max_length=255)
    # ��Ʒ������
    isxf = models.BooleanField(default=False)
    # �Ƿ��ǰ��ʷ��Ƽ���
    pmdesc = models.BooleanField(default=False)
    # �Ƿ���ָ������Ʒ
    specifics = models.CharField(max_length=64)
    # ��Ʒ����
    price = models.FloatField(default=0)
    # ��Ʒ�ļ�Ǯ
    marketprice = models.FloatField(default=1)
    # ���еļ�Ǯ
    categoryid = models.IntegerField(default=1)
    # ����id
    childcid = models.IntegerField(default=1)

    childcidname = models.CharField(max_length=128)
    # ����
    dealerid = models.IntegerField(default=1)

    storenums = models.IntegerField(default=1)
    # �����
    productnum = models.IntegerField(default=1)
    # ��Ʒ������Ҳ������Ϊ����Ʒ�ı���
    class Meta:
        db_table = 'axf_goods'
