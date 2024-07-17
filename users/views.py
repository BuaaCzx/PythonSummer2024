from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
def register(request):                                  #这个可以和下面login直接合起来了，不用再render了（render会切换界面，感觉不太理想）
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(request.POST.get('email'))              #注册的时候此处不为None 可以以此判断类型 lpr留
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)                        #系统时间可以通过前端设置，这里不太需要了 lpr留
            user_profile, create = UserProfile.objects.get_or_create(user=user)
            user_profile.login_time = user.last_login # update login time
            user_profile.save() #目前主页差不多开发完了，在templates下面，我们在想主页应该添加点什么让它看起来不空 lpr留
            return redirect('') # redirect to home_page, still don't know whether it works or not
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
        
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logout(request):
    # is this necessary?        #maybe
    logout(request)
    return redirect('login')
