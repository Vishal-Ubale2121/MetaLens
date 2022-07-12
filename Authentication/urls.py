from django.urls import path, include
from . import views as auth_views
from Screens import views as screen_views



urlpatterns = [
    path('', auth_views.login_user, name='login'),
    path('logout', auth_views.logout_user, name='logout'),
    path('index', screen_views.index, name='index'),
]