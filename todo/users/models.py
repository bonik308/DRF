from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class CustomUser(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(unique=True)

# Create your models here.
