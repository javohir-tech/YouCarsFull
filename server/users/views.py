from django.shortcuts import render

# ////////// REST FREMEWORK ////////
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# /////////// models ////////////
from .models import User

# serializers
from .serializers import SingUpSarializer, LoginSerilazer

# SIMPLE JWT
from rest_framework_simplejwt.views import TokenObtainPairView


# ////////////////////////////////////////////////////////
# /////////////////     SingUP      //////////////////////
# ////////////////////////////////////////////////////////
class SingUpView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SingUpSarializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            token = user.token()
            return Response(
                {
                    "success": True,
                    "message": "User successfully singup",
                    "data": {
                        "username": user.username,
                        "email": user.email,
                        "tokens": {
                            "access_token": token.get("access_token"),
                            "refresh_token": token.get("refresh"),
                        },
                    },
                }
            )


# ////////////////////////////////////////////////////////
# /////////////////     LOGIN      ///////////////////////
# ////////////////////////////////////////////////////////


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerilazer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]

            token = user.token()

            return Response(
                {
                    "success": True,
                    "message": "You have successfully logged in",
                    "username" :user.username,
                    "email": user.email,
                    "tokens": {
                        "access_token": token["access_token"],
                        "refresh_token": token["refresh"],
                    },
                }
            )


# Create your views here.
