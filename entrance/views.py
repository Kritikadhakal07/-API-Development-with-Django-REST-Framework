from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UniversitySerializer,ProgramSerializer
from .models import Univeristy,Program
from rest_framework.response import Response

# Create your views here.

class UniversityListView(APIView):

    def get(self,request):
        univeristy = Univeristy.objects.all()
        univeristy.programs.all()
 
class ProgramListView(APIView):

    def get(self,request):
        program = Program.objects.select_related('univeristy')
        serializer = ProgramSerializer(program,many=True)
        return Response(serializer.data)