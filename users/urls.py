from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('check_login/', views.check_login, name='check_login'),
    path('logout/', views.user_logout, name='logout')
]
