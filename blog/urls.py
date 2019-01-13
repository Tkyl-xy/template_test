"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext

#模板
from django.shortcuts import render
def index(requests):
    """视图函数：请求进来返回响应"""
    # templ = loader.get_template('index.html')
    # context = RequestContext(requests, {'contex':'www.magedu.com'})
    # return HttpResponse(templ.render(context))

    # return render(requests, 'index.html',{'contex' : 'www.baidu.com'})
    d = dict(zip('abcde', range(1,6)))
    return render(requests, 'index.html', {'dict': d})
    # return render(requests, 'index.html', {'contex':'你好', 'p1':'WTF'})  #html str
    # return HttpResponse("hello,world!!")
    # return JsonResponse({'name':'yang'})  #json str

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', index),
    path('user/', include('user.urls'))
]
