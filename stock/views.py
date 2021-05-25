from django.shortcuts import render

from django.template.loader import get_template #讓你去使用模板（外觀）
from django.http import HttpResponse
from django import template
import twstock 
from twstock import Stock 
from twstock import realtime



import twstock 
from twstock import Stock 
from twstock import realtime



def stock(request):  
#=================
#即時查詢系統 
#================
#輸入你要查詢的股票代號 
#stock_number=input("enter your stock number ") 
    stock_number=request.GET['stock_name']
#得到所有當日即時資訊 包含一個為info的字典 在原字典中
    stock_info=twstock.realtime.get(stock_number) 
#把字典裡面的字典取出來d
    info=stock_info['info']
    info_real=stock_info['realtime']
    stock={
        'a':info['time'],
        'b':info['code'],
        'c':info['name'],
        'd':info['fullname'],
        'e':info_real['best_bid_price'],
        'f':info_real['best_bid_volume'],
        'g':info_real['best_ask_price'],
        'h':info_real['best_ask_volume'],
        "i":info_real['open'],
        "j":info_real['high'],
        "k":info_real['low'],
    }
    t=get_template('real.html')
    return HttpResponse(t.render(locals()))

def first(request):
    if 'stock_name' in request.GET and request.GET['stock_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['stock_name'])
    else:
        t=get_template('first_page.html')
        return HttpResponse(t.render(locals()))

def welcome2(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        t=get_template('welcome.html')
        return HttpResponse(t.render(locals()))
    
    
def stock_list(request):
    t=get_template('stock_list.html')
    return HttpResponse(t.render(locals()))