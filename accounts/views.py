from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms  import  UserCreationFormWithEmail
def login_view(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                    username= request.POST['username']
                    password= request.POST['password']
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
            
        form=AuthenticationForm() 
        context={"form": form} 
        return render(request, 'login.html' , context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
     logout(request)
     return  redirect('/')    


def signin_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form =  UserCreationFormWithEmail(request.POST)
            if form.is_valid():
                form.save()
                return  redirect('/')  
        form = UserCreationFormWithEmail()
        context={"form": form}
        return render(request, 'signin.html', context)
    
    else:
        return  redirect('/')  

        

