from django.db import models
# from .models import static
# Create your models here.
class Recipe(models.Model):
    picture=models.ImageField( height_field=None, width_field=None, max_length=None, blank=True, null=True)
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    description=models.TextField()
    ingredients=models.CharField(max_length=100)
    process=models.TextField()
    