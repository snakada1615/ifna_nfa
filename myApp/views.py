from django.shortcuts import render
from django.core import serializers
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

def base_layout(request):
	template='myApp/base.html'
	return render(request,template)
# Create your views here.
