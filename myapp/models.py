from django.db import models

# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=250)
    body= models.TextField()
    bodylong= models.TextField(default='-')
    fb = models.CharField(default='-',max_length=250)
    tw = models.CharField(default='-',max_length=250)
    yt = models.CharField(default='-',max_length=250)
    ph = models.CharField(default='-',max_length=250)
    picurl= models.FileField()
    picname= models.FileField()
    picurl2= models.FileField(default="")
    picname2= models.FileField(default="")
    
    
    # ph = models.CharField(default='-',max_length=250)
    # ints = models.CharField(default='-',max_length=250)
    
    
    
    
    def __str__(self):
        return self.title+ ' | ' + str(self.pk)                                 #To Remove write: python manage.py makemigrations {same for adding field in db}
    
