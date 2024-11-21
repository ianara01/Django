#from django.contrib import admin
from django.urls import path
from . import views

# Create a new URL for the admin interface

app_name = "news"

urlpatterns = [
    path(" ", views.index, name="index"),
    #path('news')
    path("<int:company_id>/", views.detail, name="detail"),
]

# Add the URL path for the polls application

