from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Create your views here.
def get_students(request):
    students = Student.objects.all()
    print(students)
    html = """<table><tr><td>Fullname</td><td>Address</td></tr>"""
    for student in students:
        print(student)
        html += "<tr><td>" + student.fullname + "</td>"
        html += "<td>" + student.address + "</td></tr>"
    html += "</table>"
    return HttpResponse(html)
