from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpRequest

def reg(request):
	return HttpResponse("哈喽！欢迎来到我的主页世界!!")

def index1(request):
	d = dict(zip('abcde', range(1,6)))
	return  render(request, 'index.html', {'dict':d})
