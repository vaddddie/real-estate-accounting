from django import forms
from .models import Building

class BuildingForm(forms.ModelForm):
    objState = forms.CharField(label = 'Округ', max_length=6, required=True) #Here we can use ChoiceField
    objDistrict = forms.CharField(label = 'Район', max_length=30, required=True)
    objAddress = forms.CharField(label = 'Адрес', max_length=120, required=True)
    objType = forms.CharField(label = 'Тип объекта', max_length=20, required=True)
    objStatus = forms.CharField(label = 'Состояние объекта', max_length=20, required=True)
    objArea = forms.IntegerField(label = 'Площадь объекта', required=True)
    objOwner = forms.CharField(label = 'Собственник', max_length=50, required=True)
    objUser = forms.CharField(label = 'Фактический пользователь', max_length=50, required=True)
    objImage = forms.ImageField(label = 'Фото объекта', required=True)
    class Meta:
        model = Building
        fields = ['objState', 'objDistrict', 'objAddress', 'objType', 'objStatus', 'objArea', 'objOwner', 'objUser', 'objImage']
