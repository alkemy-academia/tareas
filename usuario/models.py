from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    documento_identidad = models.CharField(max_length=8)
