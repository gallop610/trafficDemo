from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        # 登录用户
        user = auth.authenticate(username=username, password=password)
        if(user != None):
            return redirect('/system/')

    return render(request, 'login.html')



