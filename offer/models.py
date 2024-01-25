from django.db import models

class Banner(models. Model):
    heading = models.CharField(max_length = 140)
    discription = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'off_img/', blank= True)

   

# Create your models here.
