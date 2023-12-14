from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('musicians/',include('musicians.urls')),
    path('album/',include('album.urls')),
    path('profile/<int:id>',views.profile,name='profile'),
]