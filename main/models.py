from django.db import models

# Create your models here.
class Building(models.Model):
    """ sidenotes
    We can actually use Field.choices in order to validate 
    information entered into database, but for this moment I
    dont want to do this.
    """

    objId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    objState = models.CharField(max_length=6)
    objDistrict = models.CharField(max_length=30)
    objAddress = models.CharField(max_length=120)
    objType = models.CharField(max_length=20)
    objStatus = models.CharField(max_length=20)
    objArea = models.IntegerField()
    objOwner = models.CharField(max_length=50)
    objUser = models.CharField(max_length=50)
    objImage = models.ImageField(upload_to='images/', default='default/default.png')
