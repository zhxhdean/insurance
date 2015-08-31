from django.conf.urls import url 
from .import views

urlpatterns = [
	# ex: /openapi/
	url(r'^$',views.index,name='index'),
	url(r'^get$',views.get,name='get'),
	]
