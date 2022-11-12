from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
      return render(request,'../templates/html/index.html')
def SignUp(request):
      return render(request,'../templates/html/SignUp.html')
def verifyEmail(request):
      return render(request,'../templates/html/verifyEmail.html')