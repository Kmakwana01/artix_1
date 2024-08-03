from django.urls import path
from . import views


urlpatterns = [
    path('', views.allpost , name="TECHNOLOGY" ),
    # path('technology/<slug>/', views.fullpost),
    
]
