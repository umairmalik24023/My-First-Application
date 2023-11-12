from django.db import models

# Create your models here.

class Contactform(models.Model):
    
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    body= models.TextField()
    date = models.CharField(max_length=250, default='-')
    time = models.CharField(max_length=250, default='-')
    
    # date= models.DateField()
    # time= models.TimeField()         --------> Built in Functions to show date and time in models.
    
    
    
    
    
    
    def __str__(self):
        return self.name                                #To Remove write: python manage.py makemigrations {same for adding field in db}
    
