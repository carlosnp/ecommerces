# Django
from django.urls import path, include
# Project
from .views import HomeView, InternationalizationView, ContactView

app_name = "dashboards"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("Inter18n/", InternationalizationView.as_view(), name="Inter18n"),
]