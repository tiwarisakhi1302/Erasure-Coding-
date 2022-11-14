# from django.contrib import admin
# from django.urls import path
# from erasure import views
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path("",views.index,name='home'),
#     path("SignUp",views.SignUp,name='SignUp_attempt'),
#     path("verifyEmail",views.verifyEmail,name='verifyEmail_attempt'),
#     path("success",views.success,name='success'),
#     path("token_send",views.token_send,name='token_send_attempt'),
# ]

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  index  , name="home"),
    path('verifyEmail' , verifyEmail , name="verifyEmail_attempt"),
    path('token_send' , token_send , name="token_send_attempt"),
    path('success' , success , name='success'),
    path('SignUp' , SignUp , name='SignUp_attempt')
]