from django.contrib import admin

from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("fullname", "address",)
    search_fields = ("address",)
    # list_filter = ("dob",)

admin.site.register(Teacher, TeacherAdmin)