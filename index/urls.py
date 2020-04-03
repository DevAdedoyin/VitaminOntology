from django.conf.urls import url
from .views import search
from .views import home


urlpatterns = [
                url(r'^search/', search, name='searchview'),
                url(r'^$', home, name='home')
]