from django.shortcuts import render
from .carsearch import CarSearch
from .models import *
from unitinfo.models import *
from django.http import request, response, HttpResponse
import json
import base64
# Create your views here.


# search car from img/car
def CarSerch(request):
    searchimg = request.FILES.get("searchimg", "")
    result = {}
    data = {}
    if searchimg:
        carSearchObj = CarSearch()
        resultimg = carSearchObj.carSearch(searchimg.read(), "img/car")
        cars = CarImage.objects.filter(caipiid=resultimg)
        if cars:
            data['flag'] = 0
            data['cardetails'] = {}
            data['cardetails']['carid'] = cars[0].car.id
            data['cardetails']['title'] = cars[0].car.title
            data['cardetails']['contact'] = cars[0].car.contact
            data['cardetails']['desc'] = cars[0].car.desc
            data['cardetails']['text'] = cars[0].car.text
            data['cardetails']['price'] = str(cars[0].car.lprice)+"~"+str(cars[0].car.hprice)
            reimgs = cars[0].car.carimage_set.all()
            imgarr = []
            for reimg in reimgs:
                imgarr.append(str(reimg.picture))
            data['cardetails']['reimg'] = imgarr
            data['unitdetails'] = {}
        else:
            data['flag'] = 1
            units = UnitImage.objects.filter(caipiid=resultimg)
            data['unitdetails'] = {}
            data['unitdetails']['unitid'] = units[0].unit.id
            data['unitdetails']['title'] = units[0].unit.title
            data['unitdetails']['desc'] = units[0].unit.desc
            data['unitdetails']['text'] = units[0].unit.text
            data['unitdetails']['price'] = str(units[0].unit.lprice) + "~" + str(units[0].unit.hprice)
            reimgs = units[0].unit.unitimage_set.all()
            imgarr = []
            for reimg in reimgs:
                imgarr.append(str(reimg.picture))
            data['unitdetails']['reimg'] = imgarr
            data['cardetails'] = {}
            data['cardetails']['carid'] = units[0].unit.car.id
            data['cardetails']['title'] = units[0].unit.car.title
            data['cardetails']['contact'] = units[0].unit.car.contact
            data['cardetails']['desc'] = units[0].unit.car.desc
            data['cardetails']['text'] = units[0].unit.car.text
            data['cardetails']['price'] = str(units[0].unit.car.lprice) + "~" + str(units[0].unit.car.hprice)
            reimgs = units[0].unit.car.carimage_set.all()
            imgarr = []
            for reimg in reimgs:
                imgarr.append(str(reimg.picture))
            data['cardetails']['reimg'] = imgarr
            # data['reimg'] = units[0].picture.url
        return HttpResponse(json.dumps({"result": True, "data": data, "error": ""}))
    else:
        return HttpResponse(json.dumps({"result": False, "data": "", "error": ""}))











































