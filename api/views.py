from events.models import Event
from course.models import Course
from trainer.models import Trainer
from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from .serializers import StudenSerializer
from .serializers import TrainerSerializer
from .serializers import CourseSerializer
from .serializers import EventSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class=StudenSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset =Trainer.objects.all()
    serializer_class=TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset =Course.objects.all()
    serializer_class=CourseSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset =Event.objects.all()
    serializer_class=EventSerializer