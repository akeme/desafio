from django.urls import path
from . import views

urlpatterns = [
	path('', views.consulta_list, name = 'consulta_list'),
	path('consulta/<int: pk>/', views.more_details, name = 'more_details'),
	path('consulta/new/' , views.consulta_new , name = 'consulta_new'),



]