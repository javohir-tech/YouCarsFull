from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.exceptions import ExpiredTokenError
from datetime import timedelta
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class VerifyToken(Token):
    token_type = "verify"
    lifetime = timedelta(minutes=15)

    @classmethod
    def for_user(cls, user):

        token = cls()

        token["user_id"] = str(user.id)
        token["token_type"] = "verify"
        token["current_step"] = user.auth_status

        return token

    @classmethod
    def get_user_from_token(cls, token_str):
        token = cls(token_str)

        user_id = token.get("user_id")

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise ExpiredTokenError("user topilmadi")

        return user
