from django.db import models
from django.forms import ModelForm


class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_code=models.CharField(max_length=20)
    trainer_id=models.CharField(max_length=20)
    description=models.TextField()
    syllabus=models.FileField(upload_to='documents/%Y/%m/%d')
 

    def __str__(self):
        return self.course_name