from django.db import models

# //////////// BaseModel ///////////P
from shared.models import BaseModel

# ////// user model //////////
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class USER_ROLE(models.TextChoices):
    ORDENARY_USER = "ordenary_user", "Ordenary User"
    MANAGER = "manager", "Manager"
    OPERATOR = "operator", "Operator"


class User(BaseModel, AbstractUser):

    user_role = models.CharField(
        max_length=13, choices=USER_ROLE.choices, default=USER_ROLE.ORDENARY_USER
    )
    email = models.EmailField(max_length=128 , unique=True)

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {"access_token": str(refresh.access_token), "refresh": str(refresh)}


# Create your models here.
