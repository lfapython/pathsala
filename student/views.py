from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Create your views here.
def get_all_student(request):
    students = Student.objects.all()
    return render(
        request, "list_students.html", context={"students": students}
    )


def add_student(request):
    return HttpResponse("Not Implemented")


def get_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return HttpResponse("Resource Not found.")
    # print(Student.objects.filter(id=student_id).query)
    html = f"""
    <h2>Name: {student.fullname}</h2>
    <h3>Date Of Birth: {student.dob}</h3>
    <h3>Address: {student.address}</h3>
    """
    return HttpResponse(html)


def update_student(request):
    return HttpResponse("Not Implemented")


def delete_student(request):
    return HttpResponse("Not Implemented")
