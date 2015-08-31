#-*-coding:utf8-*-
from django.shortcuts import render
from django.http import HttpResponse
import datetime 
from haystack import indexes,inputs
#models 需要使用当前app中的
from models import Category
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter 
# Create your views here.
class CategoryIndex(indexes.SearchIndex,indexes.Indexable):
	text = indexes.CharField(document=True,use_template=True)
	name = indexes.CharField(model_attr='name',faceted=True)
	pub_date = indexes.DateTimeField(model_attr='timestamp')

	def get_model(self):
		return Category
	def index_queryset(self,using=None):
		return self.get_model().objects.all()

def index(request):
	#搜索词
	words = request.GET['key'] 
	results = SearchQuerySet().filter(name__contains=(words))
	#Highlighter(my_query,html_tag='',css_class='',max_length=100)
	highlight = Highlighter(words,max_length=100)
	#(content=(words))##.facet('name',limit=10)
	#输出总条数
	counts = results.count()
	for r in results:
		r.name = highlight.highlight(r.name)
	#unicode -> string  unicodestring.endcode('utf-8') 
	#string -> unicode unicode(utf8string,'utf-8)
	return render(request,'search/search.html',{'data':results,'counts':counts})

