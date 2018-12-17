from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from rest_framework.response import Response
from .serializer_class import StudentSerializer
# Create your views here.

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serialize = StudentSerializer(students, many=True)
        return Response(serialize.data)

    def post(self):
        pass
