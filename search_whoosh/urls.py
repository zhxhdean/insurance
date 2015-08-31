#-*-coding:utf8-*-
from django.conf.urls import url 
from . import search_indexes as views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	]
