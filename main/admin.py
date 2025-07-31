from django.contrib import admin
from .models import Task, School, Student, Address, Grade, StudentProfile

# Register your models here.
admin.site.register(Task)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Address)
admin.site.register(Grade)
admin.site.register(StudentProfile)
