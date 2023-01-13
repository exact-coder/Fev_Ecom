from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.CustomerLogin, name='login'),
    path('profile/', views.ProfileView.as_view(),name='profile'),
]
