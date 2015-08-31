#-*-coding:utf8-*-
from django.contrib import admin
from .models import Category 
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','name','timestamp')
	list_filter = ['timestamp']
	search_fields = ['name','id']

admin.site.register(Category,CategoryAdmin)
