from django.shortcuts import render ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
      if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(password)
            print(username)
            
            user_obj = User.objects.filter(username = username).first()
            
            if user_obj is None :
                  messages.success(request, 'User not found')
                  return redirect('/');
            profile_obj = Profile.objects.filter(user = user_obj).first()

            if not profile_obj.is_verified :
                  messages.success(request, 'Account is not verified yet. Check your mail')
                  return redirect('/');
            user=authenticate(username=username, password=password)
            if authenticate(username=username, password=password) == False :
                  messages.success(request, 'Wrong Password')
                  return redirect('/');
            
            # login(request, user)
            return redirect('/dashboard')
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
def verify(request, auth_token):
      try:
            profile_obj = Profile.objects.filter(auth_token = auth_token).first()
            if profile_obj:
                  if profile_obj.is_verified == True :
                        messages.success(request, "Your Account is Already Verified")
                        return  redirect('/')
                  profile_obj.is_verified=True
                  profile_obj.save()
                  messages.success(request, "Congratulation your Account has been successfully Verified")
                  return  redirect('/')
            else :
                  return redirect('/error')
      except Exception as e:
            print(e)
            return redirect('/')
def error_page(request):
      return render(request, '../templates/html/error.html')
def dashboard(request):
      return render(request,'../templates/html/dashboard.html')

def send_mail_after_registration(email, token) :
      subject = 'Your account need to be verified'
      message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email]
      send_mail(subject, message, email_from, recipient_list)
