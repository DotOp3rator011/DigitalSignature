from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, unique=True)
    aadhaar = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.user.email


class Signature(models.Model):
    # user = models.OneToOneField(User, unique=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, unique=False)
    addressedTo = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    hash = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.email
