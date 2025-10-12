# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Subscriber



class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "id": "username",
            "placeholder": "ENTER USERNAME",
            "spellcheck": "false",
            "required": True,
            "class": ""
        })
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "id": "password",
            "placeholder": "ENTER YOUR PASSWORD",
            "required": True
        })
    )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'ENTER EMAIL ADDRESS', 'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'CHOOSE A USERNAME',
            'spellcheck': 'false'
        })

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
            }),
        }