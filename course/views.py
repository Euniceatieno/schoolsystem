from django.shortcuts import render,redirect
from .models import Course
from .forms import CourseForm

# Create your views here.

from django.views.generic import ListView



class CourseListView(ListView):
    paginate_by = 2
    model = Course

def index(request):
    return render(request,'index.html',{})

def course_form(request):
    if request.method == "POST":
        form = CourseForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course:course_list')
        else:
            print(form.errors)    
    else:
        form = CourseForm()
    return render(request,'course_form.html',{'form':form})
def course_list(request):
    courses=Course.objects.all()
    return render(request,'course_list.html',{'courses':courses})       
def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=='POST':
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
    else:
        form=CourseForm(instance=course)
        return render(request,'edit_course.html',{'form':form})        
        
def course_profile(request,id):
    course=Course.objects.get(id=id)
    return render(request,'course_profile.html',{'course':course})
def delete_course(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('course:course_list')
