from django.db import models

# Create your models here.

    
class naya(models.Model):
    description=models.CharField(max_length=200)
    img=models.ImageField(upload_to='Image')
