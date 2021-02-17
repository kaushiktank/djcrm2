from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Lead(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
