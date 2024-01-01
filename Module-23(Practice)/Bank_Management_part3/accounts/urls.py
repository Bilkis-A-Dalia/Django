from django.urls import path
from .views import UserRegistrationview,UserLoginView,UserLogoutView,UserBankAccountUpdateView,pass_change

urlpatterns = [
    path('register/',UserRegistrationview.as_view(),name = 'register'),
    path('login/',UserLoginView.as_view(),name = 'login'),
    path('logout/',UserLogoutView.as_view(),name = 'logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    # path('pass_update/', PasswordUpdate.as_view(), name='pass_update' )
    path('pass_update/', pass_change, name='pass_update' )
    ]
