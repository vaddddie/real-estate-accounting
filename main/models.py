from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
from django.urls import reverse

>>>>>>> calendar
=======
>>>>>>> parent of 37eaf7a (Added calendar)

# Create your models here.
class Building(models.Model):
    objId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    objState = models.CharField(max_length=6)
    objDistrict = models.CharField(max_length=30)
    objAddress = models.CharField(max_length=120)
    objType = models.CharField(max_length=20)
    objStatus = models.CharField(max_length=20)
    objArea = models.IntegerField()
    objOwner = models.CharField(max_length=50)
    objUser = models.CharField(max_length=50)
<<<<<<< HEAD
    objImage = models.ImageField(default='default/default.png', upload_to='images/')

class Workgroup(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    topic = models.CharField(max_length=50)
    date = models.DateField()
    users = models.ManyToManyField(User)
    buildings = models.ManyToManyField(Building)
=======
    objImage = models.ImageField(upload_to='images/', default='images/7fIzRQy.png')
<<<<<<< HEAD


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
>>>>>>> calendar
=======
>>>>>>> parent of 37eaf7a (Added calendar)
