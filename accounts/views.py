from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model

from .forms import LoginForm,RegisterForm
# Create your views here.

User=get_user_model()

def register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password1=form.cleaned_data.get("password1")
        password2=form.cleaned_data.get("password2")
        email=form.cleaned_data.get("email")
        
        try:
            user= User.objects.create_user(username,email,password1)
        except:
            user=None
        
        if user != None:
            login(request,user)
            return redirect("/")
        else:
            request.session['registration_error'] = 1 # 1==True

    context={
        "form":form,
    }
    return render (request,"accounts/forms.html",context)
        


def login_view(request):
    form=LoginForm(request.POST or None)

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)

        if user !=None:
            #in all the page now request.user == user
            login(request,user)
            return redirect("/")
        else:
            # attempt=request.session.get("attempt") or 0
            # request.session['attempt'] =attempt + 1
            # return redirect("invalid-password")
            request.session['invalid_user'] = 1 # 1==True
    
    context={
        "form":form,
    }

    return render (request,"accounts/forms.html",context)


def logout_view(request):
    logout(request)
    return redirect("login_view")
