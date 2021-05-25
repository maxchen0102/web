"""project_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from twstock import stock
from hello.views import hello1
from hello.views import okok,math
#from hello.views import menu 
from restaurants.views import menu ,list_restaurants
from stock.views import stock 
#from restaurants.views import welcome
from restaurants.views import comment  
from stock.views import first,welcome2
from stock.views import stock_list

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('hello/',hello1),
    re_path('(\d{1,2})/plus/(\d{1,2})',okok), 
    # 可以從網址輸入變數 給view的函數去使用 
    
    re_path('(\d{1,2})/math/(\d{1,2})',math),
    #re_path('(\d+/math/\d)',math),
    path('menu/', menu),
    
    #path('meta/',meta),
    path('welcome2/',welcome2),
    path('restaurants_list/',list_restaurants), 
    re_path('comment/(\d{1,5})', comment),
    
    path('stock/',stock),
    path('first/',first),
    path('stock_list/',stock_list),
    
    
]
