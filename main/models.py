from django.db import models

# Create your models here.
class Building(models.Model):


    def __str__(self):
        return self.Name

    # Image = models.ImageField('Cell image:', upload_to='cells/%Y-%m-%d/', default='/default_logo/favicon.ico')
