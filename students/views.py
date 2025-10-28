from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Student
from .serializers import StudentSerializer

# /api/students/  -> GET (list) & POST (create)
class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

# /api/students/adults/  -> GET only (students with age > 18)
class AdultStudentListView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(age__gt=18).order_by('id')
