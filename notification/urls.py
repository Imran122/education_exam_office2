from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

	path('notification_list/', views.notification_list, name='notification_list'),
	# path('add_notification/', views.add_notification, name='add_notification'),
	# path('notification_update/<str:pk>/', views.notification_update, name='notification_update'),


]