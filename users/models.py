from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    login_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
