from django.contrib import admin

# Register your models here.
from attendance.models import Days, Course, Student, Register, AttendanceCode

admin.site.register(Days)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Register)
admin.site.register(AttendanceCode)