from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet
from .views import EventViewSet

router=routers.DefaultRouter()
router.register('students/',StudentViewSet)
router.register('trainer/',TrainerViewSet)
router.register('course/',CourseViewSet)
router.register('event/',EventViewSet)
urlpatterns=[
    path('',include(router.urls)),
   
]