from django import forms
from django.forms.widgets import Widget
from .models import Trainer


class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields ="__all__"
        widgets = {
        'first_name':forms.TextInput(attrs={'class':'form_control'}),
        'last_name':forms.TextInput(attrs={'class':'form_control'}),
        'image':forms.FileInput(attrs={'class':'form_control'}),
        'gender':forms.Select(attrs={'class':'form_control','id':'gender',}),
        'phone_number':forms.TextInput(attrs={'class':'form_control'}),
        'email':forms.EmailInput(attrs={'class':'form_control'}),
        'city':forms.TextInput(attrs={'class':'form_control'}),
        'company':forms.TextInput(attrs={'class':'form_control'}),
        'joining_date':forms.DateTimeInput(attrs={'class':'form_control'}),
        'contract':forms.FileInput(attrs={'class':'form_control','id':'contract'}),
        'resume':forms.FileInput(attrs={'class':'form_control','id':'resume'}),
        'course_name':forms.TextInput(attrs={'class':'form_control'}),
        'salary':forms.NumberInput(attrs={'class':'form_control'}),
         }  
        labels = {
           
              'image':"Profile Photo",
               'city':"City of Residence",
             
        }


