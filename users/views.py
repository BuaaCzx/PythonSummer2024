from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
def register(request):
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
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            user_profile, create = UserProfile.objects.get_or_create(user=user)
            user_profile.login_time = user.last_login # update login time
            user_profile.save()
            return redirect('') # redirect to home_page, still don't know whether it works or not
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
        
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logout(request):
    # is this necessary?
    logout(request)
    return redirect('login')
