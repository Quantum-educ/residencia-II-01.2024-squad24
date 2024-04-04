from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Student(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    profile = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.username}"
            f"{self.created_at.strftime('%d/%m/%Y %H:%M')}"
        )
