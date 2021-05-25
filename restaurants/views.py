import restaurants
from django.shortcuts import render

from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django import template
from restaurants.models import Restaurant, Food
from restaurants.models import Comment 
from django.utils import timezone

# Create your views here.

from django.template.loader import get_template #讓你去使用模板（外觀）

'''
def menu(request):
    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    foods = [food1, food2]
    t=get_template('menu.html')
    return HttpResponse(t.render(locals()))
'''

def menu(request):
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id=request.GET['id'])
        t=get_template("menu.html")
        return HttpResponse(t.render(locals()))
    else:
        return HttpResponseRedirect("/restaurants_list/") #跳轉到另外一個要面

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        t=get_template('welcome.html')
        return HttpResponse(t.render(locals()))

def list_restaurants(request):
    restaurants = Restaurant.objects.all()# 把資料庫物件加入restaurants 
    #才可以和html的變數做結合 
    t=get_template('restaurants_list.html') #取我要的呈現網頁模式 html 
    return HttpResponse(t.render(locals()))


def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
        #我們先檢查了id參數有沒有拿到，如果沒有就重導回餐廳列表 
        # 過程是動態的 一直在跑 所以是一直return 到原來餐廳列表
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        # 把表單內容寫入html 再透過html存入變數 然後用POST取得 再存入本地變數 
        date_time = timezone.localtime(timezone.now()) # 擷取現在時間
        Comment.objects.create(visitor=visitor, email=email, content=content, date_time=date_time, restaurant=r)
        #直接在這裏 寫入資料庫
    t=get_template('comments.html')
    return render(request, 'comments.html', locals())



'''
def menu(request):
    path = request.path
    #restaurants = Restaurant.objects.all()
    restaurant=Restaurant.objects.get(id=3) # 使用get()取出欄位為3的值 
    t=get_template('menu.html')
    return HttpResponse(t.render(locals()))

'''


'''
def meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        t=get_template('welcome.html')
        return HttpResponse(t.render(locals()))
    
def list_restaurants(request):
    restaurants = Restaurant.objects.all() # 取出資料庫內容 用object物件取出全部 
    t=get_template('restaurants_list.html') #取我要的呈現網頁模式 html 
    return HttpResponse(t.render(locals())) 

'''