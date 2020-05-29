from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect #???
from django.views.decorators.clickjacking import xframe_options_exempt

def index(request,var=""):
	return HttpResponse(f"nothing now: {var}")


# def index(request):
#    return HttpResponse("hello")

# Create your views here.
