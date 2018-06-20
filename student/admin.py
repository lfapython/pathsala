from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("fullname", "address", "dob")
    search_fields = ("address",)
    list_filter = ("dob",)

admin.site.register(Student, StudentAdmin)
