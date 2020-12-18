from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget= forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Username") #charfield = textarea gibi bir şey, wtf formu ile aynı mantık
    password = forms.CharField(max_length=20,label="Password",widget= forms.PasswordInput) #text alanı gibi değil password alanı şeklinde gözükecek.
    confirm = forms.CharField(max_length=20,label="Confirm Password",widget= forms.PasswordInput)
    
    def clean(self): #Girilen password ile confirm aynı mı değil mi diye kontrol edip ona göre input gönderecek.
        username = self.cleaned_data.get("username") #username burada submit edilmeden önce alınacak
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if(password and confirm and password != confirm):
            raise forms.ValidationError("Please make sure your passwords match")
        
        values = { # Şifreler uyuşuyorsa bilgileri sözlük yardımı ile alıyoruz
            "username" : username,
            "password" : password
        }
        return values 
