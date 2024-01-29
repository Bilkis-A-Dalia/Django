from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter() #this is router kind of wifi ready

router.register('', views.AppointmentViewset) #one-->antena
urlpatterns = [
    path('', include(router.urls)),
]