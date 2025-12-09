from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_id', 'emp_name', 'designation')
    search_fields = ('emp_id', 'emp_name', 'designation')
    list_filter = ('designation',)
