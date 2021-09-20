from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GENDER=(
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("NON-BINARY","NON-BINARY"),
    ("TRANSGENDER","TRANSGENDER"),

)

class Trainer(models.Model):
    first_name = models.CharField(max_length=12 ,)
    last_name = models.CharField(max_length=20) 
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=20, choices = GENDER,default = 'FEMALE')
    phone_number = PhoneNumberField
    email =models.EmailField()
    city= models.CharField(max_length=20, default='Nairobi')
    company =models.CharField(max_length=20)
    joining_date =models.DateField(null=True)
    contract=models.FileField(upload_to='documents/%Y/%m/%d')
    resume=models.FileField(upload_to='documents/%Y/%m/%d')
    course_name =models.CharField(max_length=20)
    salary =models.BigIntegerField(null=True)
    
    
    def __str__(self):
        return self.first_name






