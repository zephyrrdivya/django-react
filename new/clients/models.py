from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=16, unique=True)
    owner = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
