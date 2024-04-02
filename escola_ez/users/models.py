from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Student(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    accept_terms = models.BooleanField()
    test_result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'accept_terms']

    def __str__(self):
        return (
            f"{self.username} "
            f"{self.created_at.strftime('%d/%m/%Y %H:%M')}"
        )
