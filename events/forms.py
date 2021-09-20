
from django.forms import ModelForm, DateInput
from django.forms.widgets import Textarea
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = '__all__'
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'description':Textarea(attrs={'class':'form_control','id':'des'}),
    }




  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)