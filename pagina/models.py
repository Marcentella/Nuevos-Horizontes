from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
        ('subdirector', 'Subdirector'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='alumno')

    def __str__(self):
        return f"{self.username} ({self.role})"
