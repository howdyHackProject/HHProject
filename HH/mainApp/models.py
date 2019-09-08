from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    interests = models.CharField(max_length=500)
    

