from django.shortcuts import render

def home_page(request):
    return render(request, 'menu.html')

def code_check(request):
    return render(request, 'codesCompare.html')

def history(request):
    return render(request, 'history.html')