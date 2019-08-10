
from django.contrib import admin
from django.urls import path
from . import views, dbviews,student_views



urlpatterns = [
    path('home/', views.home),
    path('courses/', dbviews.list_courses),
    path('addcourse/', dbviews.add_course),
    path('addnumbers/', views.add_numbers),
    path('studenthome/', student_views.home),
    path('studentadd/', student_views.add),
    path('studentlist/', student_views.list),
]
