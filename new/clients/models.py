from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
