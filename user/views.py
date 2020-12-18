from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm #şuanki klasördeki forms dosyasında RegisterForm'u al demek
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):
    #Register Yöntem 1
    form = RegisterForm(request.POST or None) #Böyle yapınca methodun post veya get olduğuunu kontrol etmek zorunda kalmıyoruz
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)
        messages.success(request, 'Succesfully Registered.')

        return redirect("index")
    context = {
        "form" : form
    }
    
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)  # Kullanıcı var mı yok mu diye kontrol eder. user diye bir değişkene attıkki kontrol edebilelim sorguda

        if (user is None): # Eğer öyle bir user yoksa demek
            messages.info(request,"Wrong Username or Password")        
            return render(request,"login.html",context)
        messages.success(request,"Login Succesfull")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context) #form is_valid değilse 
def logoutUser(request):
    logout(request)
    messages.success(request,"See you again!")
    return redirect("index")