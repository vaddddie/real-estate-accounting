from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Building

class BuildingForm(forms.ModelForm):
    objState = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите округ'})) #Here we can use ChoiceField
    objDistrict = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите район'}))
    objAddress = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите адрес'}))
    objType = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите тип объекта'}))
    objStatus = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите состояние объекта'}))
    objArea = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Введите площадь'}))
    objOwner = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите владельца'}))
    objUser = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите пользователя'}))
    objImage = forms.ImageField(required=True, widget=forms.FileInput(attrs={'accept': 'image/*', 'style': 'width: 14.5em'}))
    
    class Meta:
        model = Building
        fields = ['objState', 'objDistrict', 'objAddress', 'objType', 'objStatus', 'objArea', 'objOwner', 'objUser', 'objImage']

class Login_form(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_label'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_label'}))

    class Meta:
        model = User
        fields = ('username', 'password')
