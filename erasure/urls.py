from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('' ,  index  , name="index"),
    path('verifyEmail' , verifyEmail , name="verifyEmail_attempt"),
    path('token_send' , token_send , name="token_send_attempt"),
    path('success' , success , name='success'),
    path('dashboard', dashboard, name='dashboard_attempt'),
    path('verify/<auth_token>', verify, name="verify"),
    path('error', error_page, name="error"),
    path('upload', upload, name="upload"),
    path('files', files, name="files")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)