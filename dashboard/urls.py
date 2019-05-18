# Django
from django.urls import path, include
# Project
from .views import HomeView

app_name = "dashboards"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]