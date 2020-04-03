from django.conf.urls import url
from .views import vitamin

urlpatterns = [
                url(r'^/vitamin/(?P<result>[\w\-]+)/', vitamin, name='vitaminb5'),
]