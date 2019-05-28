from django.db import models
from carinfo.models import CarInfo

# Create your models here.

class UnitInfo(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='标题')
    desc = models.TextField(verbose_name='描述')
    text = models.TextField(verbose_name='详情文字')
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    lprice = models.DecimalField(verbose_name='最低价格', max_digits=8, decimal_places=2)
    hprice = models.DecimalField(verbose_name='最高价格', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'unitinfo'
        verbose_name = '部件表'
        verbose_name_plural = verbose_name


class UnitImage(models.Model):
    caipiid = models.CharField(verbose_name="部件图片名称", max_length=200)
    picture = models.ImageField(upload_to='img/car', verbose_name='图片')
    unit = models.ForeignKey(UnitInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit.title

    class Meta:
        db_table = 'unitimage'
        verbose_name = '部件图片'
        verbose_name_plural = verbose_name

