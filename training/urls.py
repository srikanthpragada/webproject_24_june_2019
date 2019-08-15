
from django.contrib import admin
from django.urls import path
from . import views, dbviews,student_views, rest_views


urlpatterns = [
    path('home/', views.home),
    path('courses/', dbviews.list_courses),
    path('addcourse/', dbviews.add_course),
    path('addnumbers/', views.add_numbers),
    path('studenthome/', student_views.home),
    path('studentinfo/', student_views.info),
    path('get_student/', student_views.get_student),
    path('studentadd/', student_views.add),
    path('studentlist/', student_views.list),
    path('studentdelete/', student_views.delete_student),
    path('studentedit/', student_views.edit_student),
    path('studentsearch/', student_views.search_students),
    path('ajaxdemo/', views.ajax_demo),
    path('ajaxnow/', views.ajax_now),
    path('rest/students/', rest_views.students_get_post),
    path('rest/students/<int:id>', rest_views.process_one_student),
    path('rest/client/', rest_views.client),

]
