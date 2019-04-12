from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.main),
	path('user', views.setUser),
	path('user/<str:user_name>',views.getUser),
	path('event', views.setEvent),
	path('event/<str:event_name>', views.getEvent),
]# TODO APPEND REST VIEWS
