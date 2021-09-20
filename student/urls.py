from django.urls import path
from . views import register_student
from . views import student_list
from . views import index
from . views import edit_student
from . views import student_profile
from . views import delete_student
from django.conf.urls.static import static
from django.conf import settings

app_name='student'

urlpatterns=[
    path('index/',index,name='index'),
    path('register/',register_student,name='register_student'),
    path('student_list/',student_list,name='student_list'),
    path('edit_student/<int:id>/',edit_student,name='edit_student'),
    path('student_profile/<int:id>/',student_profile,name='student_profile'),
    path('delete_student/<int:id>/',delete_student,name='delete_student'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

