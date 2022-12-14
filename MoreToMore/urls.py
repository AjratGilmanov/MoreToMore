from django.urls import path
from MoreToMoreApp import views
 
urlpatterns = [
    path("", views.index),
    path("create/", views.create),
]
