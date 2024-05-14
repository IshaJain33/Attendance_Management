from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)


admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Coordinator)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)