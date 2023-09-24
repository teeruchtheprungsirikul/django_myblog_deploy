from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'sender','email', 'detail']
        widgets = {
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control col-md-6',
                'placeholder' : "You subject here:"
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control col-md-6'
            }),
            'sender' : forms.TextInput(attrs={
                'class' : 'form-control col-md-6'
            }),
            'detail' : forms.Textarea(attrs={
                'class' : 'form-control col-md-6'
            })
        }
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]