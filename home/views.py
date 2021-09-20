from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from events.models import Event

# Create your views here.
def index(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    events=Event.objects.count()
    data={'students':students,'trainers':trainers,'courses':courses,'events':events}
       
    return render(request,'index.html',data)
