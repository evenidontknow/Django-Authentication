from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
 
def sign_up(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('home')
   else:
       form = SignUpForm()
   return render(request,'signup.html',{'form':form})
from django.contrib.auth import logout
from django.http import HttpResponse
def log_out(request):
   logout(request)
   return HttpResponse("Thanks for visiting...")
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
def log_in(request):
   if request.method == 'POST':
       print(request.POST)
       user=authenticate(request,username=request.POST['username'],
       password=request.POST['password'])
       if user is not None:
           print(user)
           login(request,user)
           return redirect('home')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('login')
   else:
       form = AuthenticationForm()
       return render(request,'login.html',{'form':form})