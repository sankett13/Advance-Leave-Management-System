from django.contrib import admin
from .models import FacultyDetail, StudentBasicDetail, StudentContactDetail, Department, LeaveHistory
# Register your models here.
admin.site.register(FacultyDetail)
admin.site.register(StudentContactDetail)
admin.site.register(StudentBasicDetail)
admin.site.register(Department)
admin.site.register(LeaveHistory)