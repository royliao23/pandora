"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from .routers import router
from app import views
urlpatterns = [
    path('', views.showmenu),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('importdatap/', views.importdata),#import people1.json with docker
    path('importdatap2/', views.importdata2),#import people2.json with docker
    path('importcompany', views.importcompany),#import companies.json with docker
    path('localimportdatap/', views.localimportdata),#import people.json from local machine
    path('localimportcompany', views.localimportcompany), # import companies.json from local machine
    path('showfriends', views.showfriends),
    path('showcompany', views.showcompany),
    path('showfood', views.showfood),
    url(r'^apishowfood/(?P<pk>\d+)/$', views.apishowfood),
    url(r'^apishowcompany/(?P<pk>\d+)/$', views.apishowcompany,name='apicomp'),
    url(r'^apishowalive/(\d+)/(\d+)$', views.apishowalive,name='apicomp'),
]
