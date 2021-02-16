from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

	path('registration/', views.registration, name='registration'),
	path('', views.login, name='login'),

]