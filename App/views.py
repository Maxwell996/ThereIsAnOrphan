from django.shortcuts import render,HttpResponseRedirect,reverse,HttpResponse

from django.views.generic import View,ListView
# Create your views here.
from django.contrib.auth.hashers import make_password #在注册时，将密码加密后存入
import App.models as models
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == 'GET':
        UserNum = request.COOKIES.get('UserNum',"")
        Password = request.COOKIES.get('Password',"")
        rep = render(request, 'Login.html', {'num':UserNum, 'password':Password})
        rep.delete_cookie('UserNum')
        rep.delete_cookie('Password')
        rep.delete_cookie('error')
        return rep

def register(request):
    return render(request,'Register.html')

def CheckID(request):
    return HttpResponse('ok')