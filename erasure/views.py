from django.shortcuts import render ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import uuid
# Create your views here.
def index(request):
      return render(request,'../templates/html/index.html')
def SignUp(request):
      return render(request,'../templates/html/SignUp.html')
def verifyEmail(request):
      if request.method == 'POST' :
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            try :
                  if User.objects.filter(username = username).first() :
                        messages.success(request, 'Username already Exist')
                        return redirect('/verifyEmail')
                  if User.objects.filter(email = email).first() :
                        messages.success(request, 'Email already Exist')
                        return redirect('/verifyEmail')

                  user_obj = User(username = username, email = email)
                  user_obj.set_password(password)
                  user_obj.save();
                  auth_token = str(uuid.uuid4())
                  profile_obj = Profile.objects.create(user=user_obj, auth_token = auth_token)
                  profile_obj.save()
                  send_mail_after_registration(email, auth_token)
                  return redirect('/token_send')
            except Exception as e:
                  print(e)
      
            
      return render(request,'../templates/html/verifyEmail.html')
def success(request):
      return render(request,'../templates/html/success.html')
def token_send(request):
      return render(request,'../templates/html/token_send.html')

def send_mail_after_registration(email, token) :
      subject = 'Your account need to be verified'
      message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email]
      send_mail(subject, message, email_from, recipient_list)
