from django import forms
from django.forms.widgets import Widget
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ="__all__"
        widgets = {
            'nationality':forms.Select(attrs={'class':'form_control','id':'nationality',}),
            'gender':forms.Select(attrs={'class':'form_control','id':'gender',}),
        } 
        labels = {
           
              'nationality':"Country of Residence",
               
        }




