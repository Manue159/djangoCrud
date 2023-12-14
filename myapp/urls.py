from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<pk>/remove/', views.employee_remove, name='employee_remove'),

    path('technicien', views.technicien_list, name='technicien_list'),
    path('technicien/new/', views.technicien_new, name='technicien_new'),
    path('technicien/<int:pk>/edit/', views.technicien_edit, name='technicien_edit'),
    path('technicien/<pk>/remove/', views.technicien_remove, name='technicien_remove'),

    path('informaticien', views.informaticien_list, name='informaticien_list'),
    path('informaticien/new/', views.informaticien_new, name='informaticien_new'),
    path('informaticien/<int:pk>/edit/', views.informaticien_edit, name='informaticien_edit'),
    path('informaticien/<pk>/remove/', views.informaticien_remove, name='informaticien_remove'),
]

