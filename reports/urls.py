from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('create/', views.report_create, name='report_create'),
    path('<int:id>/detail/', views.report_detail, name='report_detail'),
    path('<int:id>/update/', views.report_update, name='report_update'),
    path('<int:id>/delete/', views.report_delete, name='report_delete'),
]
