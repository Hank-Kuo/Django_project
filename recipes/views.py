# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.urls import reverse
def hello_view(request):
    return render(request, 'hello_django.html', {
    })
def user(request):
    return render(request, 'user.html')


def index(request):
    return render(request, 'index.html')

def normal(request):
    return render(request, '常見問題.html')

def add(request):
    name = request.POST.get('username')
    password = request.POST.get('passwd')
    user = User()
    user.username = name
    user.passwd = password
    user.save()
    print("ffff")
    return HttpResponse('新增成功！')

def getAllUser(request):
    userList = User.objects.all()
    return render(request, 'userList.html',{'users':userList})


def login(request):
    m = User.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number',8)
    return response
def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.')