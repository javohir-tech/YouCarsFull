from django.shortcuts import render

# ////////// REST FREMEWORK ////////
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# /////////// models ////////////
from .models import User

# serializers
from .serializers import SingUpSarializer


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
                        "access_token": token.get("access_token"),
                        "refresh_token": token.get("refresh"),
                    },
                }
            )


# Create your views here.
