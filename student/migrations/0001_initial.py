# Generated by Django 3.2.3 on 2021-09-10 16:58

import django.core.validators
from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('birth_date', models.DateField()),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('NON-BINARY', 'NON-BINARY'), ('TRANSGENDER', 'TRANSGENDER')], default='FEMALE', max_length=20)),
                ('student_id', models.CharField(max_length=20)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('admission_date', models.DateField()),
                ('guardian_name', models.CharField(max_length=30)),
                ('guardian_phone_number', models.CharField(max_length=20)),
                ('medical_report', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('room_number', models.PositiveSmallIntegerField()),
                ('class_name', models.CharField(max_length=20)),
                ('academic_year', models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1984), student.models.max_value_current_year])),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
