from django.urls import path, include
from . import views as auth_views
from Screens import views as screen_views



urlpatterns = [
    path('', auth_views.login_user, name='login'),
    path('logout', auth_views.logout_user, name='logout'),
    path('introduction', screen_views.introduction, name='introduction'),
    path('index', screen_views.index, name='index'),
    path('initial-screen', screen_views.initial_screen, name='initial-screen'),
]