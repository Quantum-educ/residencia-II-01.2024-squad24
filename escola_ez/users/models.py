from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class Profile(models.Model):
    ned_assessment = models.ForeignKey(
        'NedAssessment',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    vak_assessment = models.ForeignKey(
        'VAKAssessment',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class Student(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.username} – {self.created_at.strftime('%d/%m/%Y %H:%M')}"
