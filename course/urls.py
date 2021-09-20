from django.urls import path
from .views import course_form, course_profile, delete_course, edit_course
from .views import course_list
from .views import index

app_name='course'
urlpatterns=[
   path('index/',index,name='index'),
   path('course_form/',course_form,name='course_form'),
   path('course_list/',course_list,name='course_list'),
   path('edit_course/<int:id>',edit_course,name='edit_course'),
   path('course_profile/<int:id>',course_profile,name='course_profile'),
   path('delete_course/<int:id>',delete_course,name='delete_course'),
]
    