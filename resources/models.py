from django.db import models
from courses.models import Course
import uuid

# Create your models here.

class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Image(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/' ,null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)