from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    documento_identidad = models.CharField(max_length=8)
