from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        default='static/img/avatar_male.png' 
    )

    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}" .strip()
        return self.username

