from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login_view(request):
    '''登录界面'''
    return render(request,'login.html',{"title":"网上书店","content":"welcome to our bookstore"})

def login(request):
    '''处理登录功能'''
    #接收请求参数
    username=request.GET.get("username",'')
    password=request.GET.get("password","")

    #判断，稍后将改成数据库
    if username=="lyt" and password=="09118128":
        return HttpResponse("登录成功")
    return HttpResponse("登陆失败")
def register(request):
    #获取当前请求方式
    m=request.method
    if m=="GET":
        return render(request,"register.html",{"title":"Create an new account","content":""})
    else:
        return HttpResponse("Create an new account")
    #数据注册到数据库
    #定义在models中
def home(request):
    return render(request,'home.html')

def shoppingBasket(request):
    return render(request,"shoppingBasket.html")