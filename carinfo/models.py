from django.db import models
from userinfo import cargenedes
# Create your models here.

# def create_image_npy(model, filename):
#     print("aaaaaa")
#     genDesc=cargenedes.GenDesc()
#     genDesc.create_descriptors("img/car")
#     return 'img/car/'+filename


class CarInfo(models.Model):
    carid = models.CharField(max_length=10, null=False, verbose_name='车辆id')
    title = models.CharField(max_length=200, null=False, verbose_name='标题')
    contact = models.CharField(max_length=11, verbose_name='联系方式')
    desc = models.TextField(verbose_name='描述')
    text = models.TextField(verbose_name='介绍文字')
    lprice = models.DecimalField(verbose_name='最低价格', max_digits=8, decimal_places=2)
    hprice = models.DecimalField(verbose_name='最高价格', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'carinfo'
        verbose_name = '车辆信息表'
        verbose_name_plural = verbose_name


class CarImage(models.Model):
    caipiid = models.CharField(verbose_name="车辆图片名称",max_length=200)
    picture = models.ImageField(upload_to='img/car', verbose_name='图片')
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.title

    class Meta:
        db_table = 'carimage'
        verbose_name = '车辆图片'
        verbose_name_plural = verbose_name







