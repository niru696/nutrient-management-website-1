from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, default='users name')
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
