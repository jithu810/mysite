from django.shortcuts import render
from .models import enquiry
from django.shortcuts import render,redirect
# Create your views here.

# Create your views here.
def home(request):
    if  request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        enquiry(name=name,email=email,message=message).save()
        return redirect('/home')
    return render(request,'home.html')

def Next(request):
        return render(request,'home2.html')

