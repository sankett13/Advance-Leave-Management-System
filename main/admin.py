from django.contrib import admin
from .models import FacultyDetails, StudentBasicDetails, Departments, LeaveHistory
# Register your models here.
admin.site.register(FacultyDetails)
admin.site.register(StudentBasicDetails)
admin.site.register(Departments)
admin.site.register(LeaveHistory)