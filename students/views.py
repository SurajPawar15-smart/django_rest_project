from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student

def students(request):
    students={'id':1,'name':'John Doe','class':'CS'}
    return JsonResponse(students)
