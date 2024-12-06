from django.contrib import admin
from .models import Coursedetails

class CoursedetailsAdmin(admin.ModelAdmin):
    list_display = ['course_no', 'course_name', 'course_fee', 'duration', 'start_date', 'start_time', 'trainer_name', 'experience']

admin.site.register(Coursedetails, CoursedetailsAdmin)
