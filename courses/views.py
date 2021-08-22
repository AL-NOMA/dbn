from django.shortcuts import render
from .models import Course

# Create your views here.

def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)

def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    context = {'course': course }
    return render(request, 'courses/course_detail.html', context)