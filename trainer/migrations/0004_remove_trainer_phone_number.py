# Generated by Django 3.2.3 on 2021-08-12 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_alter_trainer_joining_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='phone_number',
        ),
    ]
