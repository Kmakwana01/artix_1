from django.urls import path
from . import views


urlpatterns = [
    path('', views.allpost , name="TRAVEL" ),
    # path('technology/<slug>/', views.fullpost),
]
