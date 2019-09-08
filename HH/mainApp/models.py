from django.db import models

# Create your models here.
class User(models.User):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    interests = models.CharField(max_length=500)
