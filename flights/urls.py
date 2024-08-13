from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('create/', views.flight_create, name='flight_create'),
    path('<int:id>/', views.flight_detail, name='flight_detail'),
    path('<int:id>/edit/', views.flight_update, name='flight_update'),
    path('<int:id>/delete/', views.flight_delete, name='flight_delete'),
    path('<int:id>/approve/', views.approve_flight, name='approve_flight'),
]
