from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey( User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.TextField()
    recipe_image = models.ImageField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
