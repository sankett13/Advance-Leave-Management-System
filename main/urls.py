from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    # path('student/', views.student, name='student'),
    path('FA/', views.FA, name='FA'),
    path('Hostel/', views.Hostel, name='Hostel'),
    path('login/', views.login, name='login'),
    path("leaveapply/", views.leaveapply, name='leaveapply'),
    path("faculty/", views.faculty_advisor, name='faculty_advisor'),
    path("approve_leave/<int:leave_id>/", views.approve_leave, name='approve_leave'),
    path("reject_leave/<int:leave_id>/", views.reject_leave, name='reject_leave'),
]