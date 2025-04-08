from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('hostel_incharge/', views.hostel_incharge, name='hostel_incharge'),
    path('login/', views.login, name='login'),
    path("leaveapply/", views.leaveapply, name='leaveapply'),
    path("faculty/", views.faculty_advisor, name='faculty_advisor'),
    path("approve_leave/<int:leave_id>/", views.approve_leave, name='approve_leave'),
    path("reject_leave/<int:leave_id>/", views.reject_leave, name='reject_leave'),
    path('download_leave_letter/<int:leave_id>/', views.download_leave_letter, name='download_leave_letter'),
    path('student_login/', views.student_login, name='student_login'),
    path('logout/', views.logout, name='logout'),
    path('send_email/', views.send_email, name='send_email'),
    path('parent_approve/<int:leave_id>/', views.parent_approve, name='parent_approve'),
]