# Django
from django.urls import path, include
# Project
from .views import HomeView, InternationalizationView

app_name = "dashboards"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("Inter18n/", InternationalizationView.as_view(), name="Inter18n"),
]