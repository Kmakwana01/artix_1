from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage , name="HOME"),
    path('homefurnishing/', include("homefurnishing.urls") , name="HOME FURNISHING" ),
    path('architecture/', include("architecture.urls") , name="ARCHITECTURE" ),
    path('technology/', include("technology.urls") , name="TECHNOLOGY" ),
    path('lifestyle/', include("lifestyle.urls") , name="LIFESTYLE" ),
    path('travel/', include("travel.urls") , name="TRAVEL" ),
    path('terms/', views.terms , name="TERMS" ),
    path('privacy/', views.privacy , name="PRIVACY" ),
    path('faq/', views.faq , name="FAQ" ),
    # path('fullpost/<slug>/', views.fullpost), 
    path('Contact-us/', views.contact , name="CONTACT_US" ),
    path('Contact/', views.contact),
    path('save-data/', views.save_data , name="SAVE_DATA"),
    path('architecture/<slug>/', views.architecturepost), 
    path('homefurnishing/<slug>/', views.homefurnishingpost), 
    path('technology/<slug>/', views.technologypost), 
    path('lifestyle/<slug>/', views.lifestylepost), 
    path('travel/<slug>/', views.travelpost), 
    path('search/', views.searching), 
    path('tinymce/', include('tinymce.urls')),
]
