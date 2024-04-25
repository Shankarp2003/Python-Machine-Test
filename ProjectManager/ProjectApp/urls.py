from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    path('assigned_projects/', views.assigned_projects, name='assigned_projects'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register_client/', views.register_client, name='register_client'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('client/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/', views.client_info, name='client_info'),
    path('client/<int:client_id>/add_project/', views.add_project, name='add_project'),
    path('assigned_projects/', views.assigned_projects, name='assigned_projects'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/assign_users/', views.assign_users, name='assign_users'),
    path('projects/<int:project_id>/assign_users/', views.assign_users_to_project, name='assign_users_to_project'),
]
