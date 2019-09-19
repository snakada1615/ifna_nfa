from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView
from . models import feed
import json

# Create your views here.
def index(request):
	template='myApp/index.html'
	results=feed.objects.all()
	context={
		'results':results,
	}
	return render(request,template,context)

def getdata(request):
 results=feed.objects.all()
 jsondata = serializers.serialize('json',results)
 return HttpResponse(jsondata)


class MytestView(TemplateView):
    template_name = "myApp/base.html"
