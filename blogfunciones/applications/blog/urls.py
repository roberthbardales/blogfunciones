from django.contrib import admin
from django.urls import path


from .import views
from .views import home,generales,programacion,tutoriales

app_name = "blog_app"
urlpatterns = [

    path('',home,name="index"),
    path('generales/',generales,name="generales"),
    path('programacion/',programacion,name="programacion"),
    path('tutoriales/',tutoriales,name="tutoriales"),

]