from django.conf.urls import url
from carinfo import views
urlpatterns = [
    url('search', views.CarSerch, name="searchcar"),
]
