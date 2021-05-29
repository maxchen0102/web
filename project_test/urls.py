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

#from hello.views import menu 

from stock.views import real_stock 
#from restaurants.views import welcome


from stock.views import stock_list
from stock.views import show_stock

from stock.views import Yang_get_COVID19

urlpatterns = [
    
    path('admin/', admin.site.urls),
    

    

    
    path('real_stock/',real_stock),
    path('stock_list/',stock_list),
    path('show_stock/',show_stock),


    path('COVID_EYES__/',Yang_get_COVID19),
    
    
    
]
