from django.contrib import admin
from .models import *
from userinfo import cargenedes
import json
# Register your models here.


def create_image_npy(fodername):
    genDesc=cargenedes.GenDesc()
    genDesc.create_descriptors(fodername)
    ##whr
    # genDesc = cargenedes.GenDesc()
    # genDesc.create_descriptors('img/car')
    return 'ok'


class CarInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contact')
    # class Media:
        # js = (
        #     '/static/js/kindeditor/kindeditor-all.js',
        #     '/static/js/kindeditor/lang/zh_CN.js',
        #     '/static/js/kindeditor/config.js'
        # )


class CarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caipiid', 'picture')
    exclude = ('caipiid',)

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.caipiid = obj.picture.name[8:obj.picture.name.rfind('.', 1)]
        obj.save()
        create_image_npy(obj.picture.name[8:])
        ##whr
        # create_image_npy("")


admin.site.register(CarInfo, CarInfoAdmin)
admin.site.register(CarImage, CarImageAdmin)