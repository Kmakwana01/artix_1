from django.urls import path
from . import views


urlpatterns = [
    path('', views.allpost , name="ARCHITECTURE"),
]
