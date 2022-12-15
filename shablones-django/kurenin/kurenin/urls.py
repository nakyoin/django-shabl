from nikita import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path("forms/", views.form),
]
