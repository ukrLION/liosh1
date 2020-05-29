from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.template import loader
from django.shortcuts import render, redirect #???
from django.views.decorators.clickjacking import xframe_options_exempt

from .forms import TestForms




def index(request):
	
    return render(request, "laba/1.html")


def first(request):

	return render(request, "laba/1.html")

def second(request):

	return render(request, "laba/2.html")


def third(request):
	return render(request, "laba/3.html")

def fourth(request):
	return render(request, "laba/4.html")

def fifth(request):
	return render(request, "laba/5.html")

def sixth(request):
	return render(request, "laba/6.html")

def seventh(request):
	return render(request, "laba/7.html")

def eighth(request):
	return render(request, "laba/8.html")

def ninth(request):
	return render(request, "laba/9.html")


def unit(request):
	return render(request, "laba/unit.html")


def test(request, var=" "):
	somedata = request.POST.dict
	testForm = TestForms()
	r_mathod = request.method
	answer = " "
	category = request.GET.get("cat","default")        # laba/str/?cat=str      category=str

	output = f"<h1>request: {var} with parametrs: {category} !!</h1><h2> {somedata} </h2> "

	if r_mathod == "POST":
		name = request.POST.get('name')
		age = request.POST.get('age')
		answer = f"{name} {age}"

		request.GET.dict= {"name":name,"age":age}

	var_header = "some data from python"
	var_list = ["obj1","obj2","obj3"]
	var_dict = {"key1":"obj1","key2":"obj2"}
	var_difficult = {"000":["123","456"],"111":{"k":"L"}}


	data= {"smdt":somedata,
		   "FORM":testForm,
		   "var_request": r_mathod,
		   "var_answer": answer,

		   "var1": var_header, "var2": var_list, "var3": var_dict, "var4": var_difficult}

	if str(var) == "test" or var == "test/":
		return render(request, "laba/test.html", context=data)




	return HttpResponse(output)



# def redirect(request,var=""):
#     return HttpResponseRedirect("") # if waynot exist it will be /laba/1













"""
def m304(request):
    return HttpResponseNotModified()
 
def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")
 
def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")
 
def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")
 
def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")
 
def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")
 
def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")
"""


















# def index(request):
# 	data = 0
#     return render(request,'laba/index.html',{})





##def index(request):
##    content = {
##        "hello":"hello123"
##        }
##    template = loader.get_template("laba/index.html")
##    return HttpResponse(template.render(content,request))
##
##
##
##
