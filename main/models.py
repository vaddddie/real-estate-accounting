from django.db import models
from django.contrib.auth.models import User

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
    objImage = models.ImageField(upload_to='images/', default='images/7fIzRQy.png')

class Workgroup(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    topic = models.CharField(max_length=50)
    date = models.DateField()
    users = models.ManyToManyField(User)
    buildings = models.ManyToManyField(Building)