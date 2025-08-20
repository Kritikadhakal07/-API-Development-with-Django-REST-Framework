from django.urls import path
from . import views

urlpatterns=[
    #function base views
    path('students/',views.studentsView,name='students'),
    path('students/<int:pk>',views.studentDetailView,name='student-detail'),


    #Class Based Views
    path('employees/', views.EmployeeView.as_view(),name='employees'),
    path('employees/<int:pk>',views.EmployeeDetail.as_view(),name='employee-detail'),
]