from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView
from . models import feed, FCT
import json

# Create your views here.
#def index(request):
#	template='myApp/index.html'
#	results=feed.objects.all()
#	context={
#		'results':results,
#	}
#	return render(request,template,context)

class IndexView(TemplateView):
    template_name = "myApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = FCT.objects.all()
        context["results"] = results
        return context

def getdata(request):
 results = FCT.objects.all()
 jsondata = serializers.serialize('json',results)
 return HttpResponse(jsondata)


class BaseView(TemplateView):
    template_name = "myApp/base.html"
