from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ="__all__"
        widgets = {
        'course_name':forms.TextInput(attrs={'class':'form_control'}),
        'course_code':forms.TextInput(attrs={'class':'form_control'}),
        'trainer_id':forms.TextInput(attrs={'class':'form_control'}),
        'description':forms.Textarea(attrs={'class':'form_control','id':'des'}),
        'syllabus':forms.FileInput(attrs={'class':'form_control','id':'formFile'}),
       
         }  
        labels = {
              'trainer_id':"Course trainer ID",
               'description':"Course description",
             
        }




        


