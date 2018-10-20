from django.http import HttpResponse
from django.conf.urls import url,include
from django.shotcuts import render,redirect





#/list--url
def list(reqest):
	return render(request,'booktest/list.html'{})
#/index---url
def index(resquest):
	'''index Views(首页)'''
	return HttpResponse('index')


#addUI---url
def addUI(request):
	return render(request,'booktest/addui.html',{})

#add---url
def add(request):
	return redirect(request,'booktest/list.html',{})
