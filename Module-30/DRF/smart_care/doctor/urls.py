from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter() #this is router

router.register('specialization', views.SpecializationViewset) #one-->antena
router.register('designation', views.DesignationViewset) #one-->antena
router.register('available_time', views.AvailableTimeViewset) #one-->antena
router.register('list', views.DoctorViewset) #one-->antena
router.register('reviews', views.ReviewViewset) #one-->antena
urlpatterns = [
    path('', include(router.urls)),
]