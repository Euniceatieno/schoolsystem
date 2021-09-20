import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from django.core.validators import MaxValueValidator, MinValueValidator
#import phonenumber


from django.db import models

# Create your models here.



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)



GENDER=(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("NON-BINARY","NON-BINARY"),
    ("TRANSGENDER","TRANSGENDER"),

)

class Student(models.Model):
    first_name = models.CharField(max_length=12) 
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    birth_date =models.DateField(null=True)
    nationality = CountryField()
    gender = models.CharField(max_length=20, choices = GENDER,default='FEMALE')
    student_id = models.CharField(max_length=20)
    phone_number = PhoneNumberField()
    admission_date =models.DateField(null=True)
    guardian_name = models.CharField(max_length=30)
    guardian_phone_number = models.CharField(max_length=20)
    medical_report=models.FileField(upload_to='documents/%Y/%m/%d')
    room_number = models.PositiveSmallIntegerField()
    class_name =models.CharField(max_length=20)
    academic_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984),max_value_current_year])
    email =models.EmailField()
    city =models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')

    
    def __str__(self):
        return self.first_name


     