from django.contrib import admin

from .models import Student, StudentInfo

class StudentAdmin(admin.ModelAdmin):
    list_display = ("fullname",)
    # search_fields = ("address",)
    # list_filter = ("dob",)


class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ("student", "crn", "dob")

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
