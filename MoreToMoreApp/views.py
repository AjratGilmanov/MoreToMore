from datetime import date
from django.shortcuts import render
from .models import Student, Course
from django.http import HttpResponseRedirect
  
# получение данных из бд
def index(request):
    # фильтрация
    students = Student.objects.all()
    return render(request, "index.html", {"students":students})
 
# добавление данных в бд 
def create(request):
    initialize()
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        student = Student()
        student.name = request.POST.get("name")
        course_ids = request.POST.getlist("courses")
        student.save()
        # получаем все выбранные курсы по их id
        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses,  through_defaults={"date": date.today(), "mark":0})
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    courses = Course.objects.all()
    return render(request, "create.html", {"courses": courses})
 
def initialize():
    # Student.objects.all().delete()
    # Course.objects.all().delete()
    if Course.objects.all().count() == 0:
        Course.objects.create(name = "Python")
        Course.objects.create(name = "Django")
        Course.objects.create(name = "FastAPI")