from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name='courses'),
    path('course/<slug:slug>', views.course_detail, name='course_detail'),
]