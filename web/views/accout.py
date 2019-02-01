# Author: harry.cai
# DATE: 2018/10/8
from django.shortcuts import HttpResponse, render, redirect
from rbac import models
from rbac.service.init_permission import *


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()

    if not current_user:

        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    init_permission(current_user, request)

    return redirect('/customer/list/')


