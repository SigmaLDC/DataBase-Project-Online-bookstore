from django.shortcuts import render
from django.http import HttpResponse
from bookstore1.models import logged_users
from bookstore1.models import book_information
# Create your views here.



def login_view(request):
    '''登录界面'''
    return render(request,'login.html',{"title":"网上书店","content":"welcome to our bookstore"})

def login(request):
    '''处理登录功能'''
    #接收请求参数
    username=request.GET.get("username",'')
    password=request.GET.get("password","")
    result = logged_users.objects.filter(name=username)
    if password == result.password:
        return render(request,'main.html')
    else:
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

def search(request):
    '''
    处理查找功能
    '''
    requirement = request.GET.get("label",'')
    name = request.GET.get("name",'')
    return render(request, 'search.html')


'''
def search_output(request):
    requirement = request.POST['label']
    name = request.POST['name']
    if requirement == "作者":
        result = book_information.objects.filter(Author=name)
    elif requirement == "ISBN":
        result = book_information.objects.filter(ISBN=name)
    elif requirement == "书名":
        result = book_information.objects.filter(BookName=name)
    elif requirement == "评分大于":
        result = book_information.objects.filter(Score__gte=name)
    elif requirement == "评分小于":
        result = book_information.objects.filter(Score__ite=name)
    elif requirement == "价格小于":
        result = book_information.objects.filter(Score__ite=name)
    elif requirement == "价格大于":
        result = book_information.objects.filter(Score__gte=name)
    return render(request, 'search_output.html',context={'data':result})
    '''

def FAQ(request):
    return render(request, 'FAQ.html')

