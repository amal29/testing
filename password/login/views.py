from django.shortcuts import render
from django.core.mail import  send_mail
from .models import *
from django.utils.crypto import get_random_string


# Create your views here.
def show(request):
    if request.method=='POST':
        nm=request.POST['username']
        pa=request.POST['pass']
        ob=tbl()
        ob.name=nm
        ob.pas=pa
        ob.save()
        return render(request, 'res.html')

    return render(request,'index.html')



def email(request):
    return render(request,'email.html')


def reset(request):
    if request.method=='POST':
        recepient = request.POST['em']
        otp = get_random_string(6, allowed_chars='0123456789')
        send_mail('Reset Password','OTP for Reseting Your Password is '+otp ,'amalsankar29@gmail.com',[recepient],fail_silently=False)
        return render(request,'reset.html')

