from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import difflib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods


def home_page(request):
    return render(request, 'menu.html')


def code_check(request):
    return render(request, 'codesCompare.html')


def history(request):
    return render(request, 'history.html')

