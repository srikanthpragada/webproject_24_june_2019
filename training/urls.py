
from django.contrib import admin
from django.urls import path
from . import views
from . import dbviews


urlpatterns = [
    path('home/', views.home),
    path('courses/', dbviews.list_courses),
    path('addcourse/', dbviews.add_course),
]
