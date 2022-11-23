from django.db import models
from django.contrib.auth.models import User  #Importing User


class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# from djongo import models

# class myUser(models.Model) :
#     username = models.CharField(max_length=100)



# class Profile(models.Model) :
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     auth_token = models.CharField(max_length=100)
#     is_verified=models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)


    