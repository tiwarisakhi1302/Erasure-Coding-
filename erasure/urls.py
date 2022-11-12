from django.contrib import admin
from django.urls import path
from erasure import views
urlpatterns = [
    path("",views.index,name='home'),
    path("SignUp",views.SignUp,name='SignUp_attempt'),
    path("verifyEmail",views.verifyEmail,name='verifyEmail_attempt'),
    path("success",views.success,name='success'),
    path("token",views.token,name='token'),
]
