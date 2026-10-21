from django.urls import path
from .views import (
    webapp
)


urlpatterns = [
    path("", webapp, name="webapp"),
]