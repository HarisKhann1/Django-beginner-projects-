from django.db import models

# Create your models here.
class img(models.Model):
    img_name = models.CharField(max_length=300)
    img_desc = models.CharField(max_length=300)

    def __str__(self):
        return self.img_name