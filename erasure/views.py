from django.shortcuts import render ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.uploadedfile import *
from django.core.files import File
from django.shortcuts import redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from algo import *
from list_of_files import *
from subprocess import run,PIPE
import os
import sys
def index(request):
      if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username = username).first()

            if user_obj is None :
                  messages.success(request, 'User not found')
                  return redirect('/')

            profile_obj = Profile.objects.filter(user = user_obj).first()

            if not profile_obj.is_verified :
                  messages.success(request, 'Account is not verified yet. Check your mail')
                  return redirect('/')

            user = authenticate(username=username, password=password)

            if user is None :
                  messages.success(request, 'Wrong Password')
                  return redirect('/')
            request.session['username'] = username
            print(request.session['username'])
            return redirect('/dashboard')
      return render(request,'../templates/html/index.html')


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
                  user_obj.save()
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
      if request.method=="POST" :
            file=request.POST.get('myfile')

      return render(request,'../templates/html/dashboard.html')

def upload(request):
      global os
      import os
      from reedsolo import RSCodec
      from pathlib import Path
      username = request.session['username']
      fdata = request.FILES['myfile'].read()
      fname = request.FILES['myfile'].name
      fname = fname.removesuffix(".txt")
      os.chdir('./media')
      try:
            os.mkdir(username)
            os.chdir(username)
            try :
                  os.mkdir(fname)
                  os.chdir('../')
                  os.chdir('../')
            except :
                  os.chdir('../')
      except:
            os.chdir('../')
      fli="./media/"+username+"/"+fname+'/'+fname+".txt"

      str1 = bytes.decode(fdata)

      print(fdata)

      f = open(fli, "w")
      f.write(str1)

      size_of_file=len(str1)

      if(2*size_of_file > 254) :    #127
            rsc = RSCodec(254)
      else :
            rsc = RSCodec(2*size_of_file)

      b_str=bytes(str1, 'utf-8')

      # # print(b_str)

      encoded_msg= rsc.encode(b_str)

      # # print(encoded_msg)

      parity_block = encoded_msg.removeprefix(b_str)

      # # print(parity_block)

      # # print(size_of_file)

      os.chdir('./media')
      os.chdir(username)
      os.chdir(fname)
      fle=fname+"_encode.bin"
      f = open(fle, "wb")

      f.write(parity_block)

      f.close()

      size = str(size_of_file)
      fli1=fname+"_original_len.txt"

      f=open(fli1, "w")
      f.write(size)
      f.close()

      os.chdir('../')
      os.chdir('../')
      os.chdir('../')
      os.chdir('../')
      print('File is Encoded successfully')
      return redirect('/dashboard')

def recover(request):
      if request.method == 'POST':
            username = request.session['username']
            fname=request.POST.get('file_to_recover')
      print('Recovering')

      from reedsolo import RSCodec
      from pathlib import Path
      # from encode import size_of_file
      fli = "./media/"+username+'/'+fname+'/'+fname+".txt"

      fle="./media/"+username+'/'+fname+'/'+fname+"_encode.bin"

      f = open(fle, 'rb')

      parity=f.read()

      f.close()

      fle_s ="./media/"+username+'/'+fname+'/'+fname+"_original_len.txt"
      f = open(fle_s, 'r')
      size = f.read()

      size_of_file = int(size)

      f.close()
      # print(parity)

      temp=""

      for i in range(size_of_file) :
            temp = temp + 'X'

      t = bytes(temp, encoding='latin-1')

      # print(t)

      if(2*size_of_file> 254) :    #127
            rsc = RSCodec(254)
      else :
            rsc = RSCodec(2*size_of_file)

      temp1 = t + parity

      # print(temp1)

      # Decoding (repairing)

      decoded_msg, decoded_msgecc, errata_pos = rsc.decode(temp1)

      # print(decoded_msg)

      data = str(decoded_msg)

      data = data.removeprefix("bytearray(b'")
      data = data.removesuffix("')")

      # print(data)

      fli="./media/"+fname+".txt"
      f = open(fli, "w")
      f.write(data)

      print('File is decoded successfully')
      redirect('/dashboard')
      # print(data)





def download(request):
      print('Downloading')

def files(request):
      user = request.session['username']
      global os
      # import os
      path=r'C:\\Users\\yashm\\OneDrive\\Desktop\\minor codeeee\\media\\'
      path=os.path.join(path,user)
      files_uploaded=os.listdir(path)
      for fl in files_uploaded:
            print(fl)
      return render(request,'../templates/html/dashboard.html',{'list_name':files_uploaded})

def send_mail_after_registration(email, token) :
      subject = 'Your account need to be verified'
      message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email]
      send_mail(subject, message, email_from, recipient_list)

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
