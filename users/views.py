from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
import json

from django.views.decorators.http import require_http_methods


@csrf_protect
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if email:
            # Register
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'failure', 'message': '该用户名已存在'})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({'status': 'failure', 'message': '该邮箱已被注册'})
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return JsonResponse({'status': 'success', 'message': '注册成功', 'username': username})
        else:
            # Login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': '登录成功', 'username': username})
            else:
                return JsonResponse({'status': 'failure', 'message': '用户名或密码错误'})

    return render(request, 'users/login.html')


@login_required
@require_http_methods(["GET"])
def user_logout(request):
    logout(request)
    return JsonResponse({'status': 200, 'logout': True})


def check_login(request):
    if request.user.is_authenticated:
        return JsonResponse({'status': 'success', 'login': True, 'username': request.user.username})
    else:
        return JsonResponse({'status': 'success', 'login': False})
