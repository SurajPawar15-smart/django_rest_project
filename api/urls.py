from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.studentsView, name='studentsList'), # handle GET and POST
    path('students/<int:pk>/', views.StudentDetailView), # GET, PUT, DELETE

    # Class based views URLs
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view())

]