from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student_login',views.student_login,name='student_login'),
]