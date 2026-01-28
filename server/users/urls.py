from django.urls import path
from .views import SingUpView, LoginView, LogOutView, ForgetPasswordView, CodeVerifyView

urlpatterns = [
    path("singup/", SingUpView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogOutView.as_view()),
    path("forget/", ForgetPasswordView.as_view()),
    path("verify/", CodeVerifyView.as_view()),
]
