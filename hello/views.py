from django.http import HttpResponse
from django import template


from django.shortcuts import render
from django.http import HttpResponse




#=================================================================

#=================================================================
from django.template.loader import get_template #讓你去使用模板（外觀）


def menu(request):
    
    food = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    t=get_template('menu.html')
    return HttpResponse(t.render(locals()))
#=================================================================

from django import template
from django.template.loader import get_template #讓你去使用模板（外觀）

def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b # 使用locals()  s就變成 key 傳入math.html對應的key 而value 就是a+b 
    d = a - b
    p = a * b
    q = a / b
    t = get_template('math.html') 
    #直接使用get_template 去取用math 模板
    #因為math.html 和views 在同個資料夾下 所以直接使用math.html即可 
    return HttpResponse(t.render(locals()))

#Template物件中的render方法，執行的就是填寫的動作 把URL傳過來的值填寫到模板中 
#=================================================================

# Create your views here.
def hello1(request):
    return HttpResponse("Hello Django")


def okok(request,a,b):
    result=int(a)+int(b) 
    return HttpResponse(str(result)) 
#被urls.py 給request  到這裡取用函式 
#回傳東西到網路上

#=================================================================
#用open function去打開templates 裡面的 math.html 
#分離了template 到application底下
'''
from django import template

def math(request, a, b):
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    #用open function去打開templates 裡面的 math.html
    with open('hello/templates/math.html', 'r') as reader: 
        #open路徑 因為預設的DIR只有最外層的打開而以 就是manage.py這層 所以要加上我的application名稱
        t = template.Template(reader.read())
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q})
    return HttpResponse(t.render(c))
    '''
#=================================================================



'''
def math(request,a,b):
    a=int(a) 
    b=int(b)
    s=a+b 
    d=a-b
    p=a*b
    q=a/b
    html = '<html>sum={s}<br>dif={d}<br>pro={p}<br>quo={q}</html>'.format(s=s, d=d, p=p, q=q)

    return HttpResponse(html)

''' 


'''
# 把樣板寫在view 中 後來要去把樣板獨立出來

from django import template

def math(request, a, b):
    a = float(a)
    b = float(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    t = template.Template('<html>sum={{s}}<br>diffuckyou={{d}}<br>pro={{p}}<br>quo={{q}}</html>')
    c = template.Context({'s': s, 'd': d, 'p': p, 'q': q}) #樣板的內容
    return HttpResponse(t.render(c))# render為填寫動作 把樣版內容填寫入t的html樣板中

''' 