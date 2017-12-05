from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    housenum = models.CharField(max_length = 4, unique = False, blank = False, null = False, default="НЕТ")
    flatnum = models.IntegerField(null = False, default=0)
    
    pass
