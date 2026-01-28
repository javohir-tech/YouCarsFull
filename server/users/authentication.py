from rest_framework_simplejwt.authentication import JWTAuthentication
from .tokens import VerifyToken
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from django.core.exceptions import ObjectDoesNotExist


class VerifyTokenAuthentication(JWTAuthentication):

    def get_validated_token(self, raw_token):
        try:
            return VerifyToken(raw_token)
        except Exception as e:
            raise AuthenticationFailed(f"Token is invalid {e}")

    def get_user(self, validated_token):

        try:
            user_id = validated_token.get("user_id")
            if user_id is None:
                raise AuthenticationFailed(f"token ichida {user_id} yo'q")

            user = User.objects.get(id=user_id)

            if user.auth_status != validated_token.get("current_step"):
                raise AuthenticationFailed("Token is invalid or has expired.")

            return user
        except ObjectDoesNotExist:
            raise AuthenticationFailed("user topimadi")
        except Exception as e:
            raise AuthenticationFailed(
                f"Authentication credentials were not provided or are invalid."
            )
