from django.db import models

# Create your models here.
class Place(models.Model):
    name= models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    def __str__(self):
         return self.name
class Picture(models.Model):
    name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()
    def __str__(self):
        return self.name




