from django.http import HttpResponse
from django.conf.urls import url,include
from django.shotcuts import render





#/list--url
def list(reqest):
	return render(request,'booktest/list.html'{})
#/index---url
def index(resquest):
	'''index Views(首页)'''
	return HttpResponse('index')

def main():
	'''main function'''
	pass


if __name__ == '__main__':
	main()

