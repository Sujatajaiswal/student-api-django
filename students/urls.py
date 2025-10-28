from django.urls import path
from .views import StudentListCreateView, AdultStudentListView

urlpatterns = [
    path("students/", StudentListCreateView.as_view()),
    path("students/adults/", AdultStudentListView.as_view()),
]
