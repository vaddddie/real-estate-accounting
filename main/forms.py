from django import forms
from .models import Building, Event

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
