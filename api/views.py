from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
     students={'id':1,'name':'John Doe','class':'CS'}
     return JsonResponse(students)
