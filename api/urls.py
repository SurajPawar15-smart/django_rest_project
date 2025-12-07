from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.studentsView, name='studentsList'), # handle GET and POST

]