from django.db import models

class BookInfoManager(models.Manager): #代替objects管理器
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.breab = 0
        b.bcomment = 0
        b.isDelete = False
        return b

class BookInfo(models.Model):  #模型类
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    breab = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'

    books1 = models.Manager()
    books2 = BookInfoManager()

    def __str__(self):
        return self.btitle

    @classmethod
    def create(cls,btitle,bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.breab=0
        b.bcomment=0
        b.isDelete=False
        return b






class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.hname