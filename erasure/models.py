from django.db import models
from django.contrib.auth.models import User  #Importing User


class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Files(models.Model) :
    # user=models.Prfi
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='text_files/', null=True, default=True)

    