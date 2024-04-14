from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Profile(models.Model):
    pass


class Student(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return (
            f"{self.username} {self.created_at.strftime('%d/%m/%Y %H:%M')}"
        )
