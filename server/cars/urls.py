from django.urls import path

# //////////////////////// VIEWS ///////////////
from .views import GetAvtoTypesView, GetMarkaWithTypeView, GetModelsWithMarkaView

urlpatterns = [
    path("avtotype/", GetAvtoTypesView.as_view()),
    path("marka/", GetMarkaWithTypeView.as_view()),
    path("models/", GetModelsWithMarkaView.as_view()),
]
