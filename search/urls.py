from django.conf.urls import url
from .views import Classes
from .views import Vitamins

urlpatterns = [
                url(r'^list/(?P<vitamins>[\w\-]+)/', Classes, name='ontclass'),
                url(r'^category/', Vitamins, name='category')
]