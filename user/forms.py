from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, FileInput, EmailInput
from django import forms

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')
        widgets={
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username', 'size':'110'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email', 'size':'110'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name', 'size':'110'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name', 'size':'110'}),
        }

CITY=[
    ('Istanbul', 'Istanbul'), ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'), ('Denizli', 'Denizli'),
    ('Mugla', 'Mugla'),('Aydın', 'Aydın')]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone', 'address', 'city', 'country', 'image')
        widgets={
            'phone':TextInput(attrs={'class':'input', 'placeholder':'phone', 'size':'110'}),
            'address':TextInput(attrs={'class':'input', 'placeholder':'address', 'size':'110'}),
            'city':Select(attrs={'class':'input', 'placeholder':'city'},choices=CITY),
            'country':TextInput(attrs={'class':'input', 'placeholder':'country', 'size':'110'}),
            'image':FileInput(attrs={'class':'input', 'placeholder':'image'}),
        }

