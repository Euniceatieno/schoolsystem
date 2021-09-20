from django.urls import path
from .views import delete_trainer, edit_trainer, register_trainer, trainer_list, trainer_profile

app_name="trainer"

urlpatterns=[
    path('register_trainer/',register_trainer,name='register_trainer'),
    path('trainer_list/',trainer_list,name='trainer_list'),
    path('edit_trainer/<int:id>',edit_trainer,name='edit_trainer'),
    path('trainer_profile/<int:id>',trainer_profile,name='trainer_profile'),
    path('delete_trainer/<int:id>',delete_trainer,name='delete_trainer'),
    
]