from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email')
        if email:
            # Register
            if User.objects.filter(username=username).exists():
                return render(request, 'users/login.html', {'error': '该用户名已存在'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'users/login.html', {'error': '该邮箱已被注册'})
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home_page')
        else:
            # Login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
