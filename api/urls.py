from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet, basename='employees')

urlpatterns=[
    #function base views
    # path('students/',views.studentsView,name='students'),
    # path('students/<int:pk>',views.studentDetailView,name='student-detail'),


    #Class Based Views
#     path('employees/', views.Employees.as_view(),name='employees'),
#  path('employees/<int:pk>',views.EmployeeDetail.as_view(),name='employee-detail'),

path('',include(router.urls))

]