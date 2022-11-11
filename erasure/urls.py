from django.contrib import admin
from django.urls import path
from erasure import views
urlpatterns = [
    path("",views.index,name='home'),
    path("SignUp",views.SignUp,name='SignUp')
]
