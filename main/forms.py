from django import forms
from .models import Building,Workgroup
from django.contrib.auth.models import User

class BuildingForm(forms.ModelForm):
    objState = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите округ'})) #Here we can use ChoiceField
    objDistrict = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите район'}))
    objAddress = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите адрес'}))
    objType = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите тип объекта'}))
    objStatus = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите состояние объекта'}))
    objArea = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Введите площадь'}))
    objOwner = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите владельца'}))
    objUser = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите пользователя'}))
    objImage = forms.ImageField(required=True)
    
    class Meta:
        model = Building
        fields = ['objState', 'objDistrict', 'objAddress', 'objType', 'objStatus', 'objArea', 'objOwner', 'objUser', 'objImage']
        
class WorkgroupForm(forms.ModelForm):
    topic = forms.CharField(required=True, max_length=50)
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    buildings = forms.ModelMultipleChoiceField(required=True, queryset=Building.objects.all(), widget=forms.CheckboxSelectMultiple)
    users = forms.ModelMultipleChoiceField(required=True, queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Workgroup
        fields = ['topic', 'date', 'buildings', 'users']
