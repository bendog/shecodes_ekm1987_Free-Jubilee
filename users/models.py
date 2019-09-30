from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    required_fields = ["email", "first_name", "last_name"]

    def __str__(self):
        return self.email
