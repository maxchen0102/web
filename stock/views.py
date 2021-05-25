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
from stock.models import StockTable2330
from stock.models import Stock_list # 引入10支股票選項 在資料庫中 model 



def stock_info(request):
    if 'id' in request.GET and request.GET['id'] == '1':
        content=StockTable2330.objects.all()
        t=get_template('stock_info.html')
        return HttpResponse(t.render(locals()))
    else:
        t=get_template('stock_list.html')
        return HttpResponse(t.render(locals()))



def first(request):
    if 'stock_name' in request.GET and request.GET['stock_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['stock_name'])
    else:
        t=get_template('first_page.html')
        return HttpResponse(t.render(locals()))
'''
def welcome2(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        t=get_template('welcome.html')
        return HttpResponse(t.render(locals()))
''' 

def stock_list(request):
    r1=Stock_list.objects.all() # 把10個股票的資訊 存入choice 給html使用
    t=get_template('stock_list.html')
    return HttpResponse(t.render(locals()))



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