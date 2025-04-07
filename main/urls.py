from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    # path('student/', views.student, name='student'),
    path('fa/', views.FA, name='FA'),
    path('hostel/', views.hostel, name='hostel'),
    path('login/', views.login, name='login'),
    path("leaveapply/", views.leaveapply, name='leaveapply'),
    path("faculty/", views.faculty_advisor, name='faculty_advisor'),
    path("approve_leave/<int:leave_id>/", views.approve_leave, name='approve_leave'),
    path("reject_leave/<int:leave_id>/", views.reject_leave, name='reject_leave'),
    path('download_leave_letter/<int:leave_id>/', views.download_leave_letter, name='download_leave_letter'),
]