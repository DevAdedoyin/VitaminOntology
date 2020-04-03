"""VitaminOntology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('index.urls')),
    url(r'^', include('search.urls')),
    url(r'^VitaminA', include('VitaminA.urls')),
    url(r'^VitaminB1', include('VitaminB1.urls')),
    url(r'^VitaminB2', include('VitaminB2.urls')),
    url(r'^VitaminB3', include('VitaminB3.urls')),
    url(r'^VitaminB5', include('VitaminB5.urls')),
    url(r'^VitaminB6', include('VitaminB6.urls')),
    url(r'^VitaminB7', include('VitaminB7.urls')),
    url(r'^VitaminB9', include('VitaminB9.urls')),
    url(r'^VitaminB12', include('VitaminB12.urls')),
    url(r'^VitaminC', include('VitaminC.urls')),
    url(r'^VitaminD', include('VitaminD.urls')),
    url(r'^VitaminE', include('VitaminE.urls')),
    url(r'^VitaminK', include('VitaminK.urls')),
]
