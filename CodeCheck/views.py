from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/users/login/')
def home_page(request):
    return render(request, 'menu.html')


def code_check(request):
    return render(request, 'codesCompare.html')


@login_required(login_url='/users/login/')
def history(request):
    return render(request, 'history.html')
