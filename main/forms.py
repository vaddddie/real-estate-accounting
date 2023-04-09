from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
<<<<<<< HEAD
from .models import Building,Workgroup
from django.contrib.auth.models import User
=======
from .models import Building, Event
>>>>>>> calendar

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
<<<<<<< HEAD
        
class WorkgroupForm(forms.ModelForm):
    topic = forms.CharField(required=True, max_length=50)
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    buildings = forms.ModelMultipleChoiceField(required=True, queryset=Building.objects.all(), widget=forms.CheckboxSelectMultiple)
    users = forms.ModelMultipleChoiceField(required=True, queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Workgroup
        fields = ['topic', 'date', 'buildings', 'users']


class Login_form(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_label'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_label'}))

    class Meta:
        model = User
        fields = ('username', 'password')
=======


class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
>>>>>>> calendar
