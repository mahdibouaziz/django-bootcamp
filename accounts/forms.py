from django.contrib.auth import get_user_model
from django import forms


#we just import our User Model using this method (This is the best way to import it )
User=get_user_model()

class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )
    )
    password2=forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-confirm-password"
            }
        )
    )

    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists, please pick another")
        return username
    
    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already registred")
        return email




class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )
    )

    #Check for the username
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username


    #the last method that's gonna be called after cleaning each attribute indivudually
    # def clean(self):
    #     #check the user + the password exists together
    #     username=self.cleaned_data.get("username")
    #     password=self.cleaned_data.get("password")
        



