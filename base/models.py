from django.contrib.auth.models import User
from django.db import models
import logging

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    name = models.CharField(max_length=50)
    step_no = models.IntegerField()
    step = models.TextField()
    time = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
