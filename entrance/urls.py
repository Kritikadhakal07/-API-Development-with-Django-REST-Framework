
from django.urls import path
from . import views



urlpatterns = [
    path('universities/', views.UniversityListView.as_view(), name="universities"),
    path('programs/', views.ProgramListView.as_view(), name="programs"),
]