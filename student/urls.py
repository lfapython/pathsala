
from django.urls import path

from .views import (
    get_all_student,
    get_student,
    add_student,
    update_student,
    delete_student
)

urlpatterns = [
    path("", get_all_student),
    path("<int:student_id>", get_student),
]
