from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.FileField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)