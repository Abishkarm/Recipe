from django.db import models

# Create your models here.
class Recipe(models.Model):
    Picture=models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    Name=models.CharField(max_length=30)
    Category=models.CharField(max_length=30)
    Description=models.TextField()
    Ingrdients=models.CharField(max_length=100)
    Process=models.TextField()
    