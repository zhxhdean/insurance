#-*-coding:utf8-*-
from django.db import models

# Create your models here.

#分类
class Category(models.Model):
	class Meta:
		db_table = "insurance_category"
		ordering = ['id']#desc use -,default asc
	p_id = models.IntegerField()
	name = models.CharField(max_length=50)
	timestamp = models.DateTimeField()
	def __unicode__(self):
		return self.name
