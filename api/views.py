from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import generics,mixins,viewsets
from django.shortcuts import get_object_or_404
#Here we were manually serailizing the query set by converting them in list and
#returning it as json response

# def studentsView(request):
#    students=Student.objects.all()
#    student_list = list(students.values())
#    return JsonResponse(student_list,safe=False)

#This is the function based views
# @api_view(['GET','POST'])
# def studentsView(request):
#    #  print(request)
#     """
#     This view function handles the HTTP GET request to get all the data
#     from the student table. It returns a JSON response containing the serialized
#     data.

#     Parameters:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         Response: The HTTP response object containing the serialized data.
#     """

#     if request.method == 'GET':
#         #Get all the data from the student table
#         students=Student.objects.all()
#         serializer = StudentSerializer(students,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         #Create a new student(Post)
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def studentDetailView(request,pk):
#     try:
#         student=Student.objects.get(pk=pk)

#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# # Create  a Class based views

# class EmployeeView(APIView):

#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
 
#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,stataus=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):
# #go to the data base and bring the employee
# #  based on the primary key that we pass.
#     def get_object(self,pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
            
#             return employee
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self,request,pk):

#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
          
#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
"""

"""
# Generic Class Based Views

# class Employees(generics.ListAPIView,generics.CreateAPIView):
class Employees(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer





# Generic Class Based Views
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # Based on the primary key we want to get the details 
    lookup_field = 'pk '
"""



# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def create(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self,request,pk=None):
#         queryset = Employee.objects.all()
#         employee = get_object_or_404(queryset,pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def update(self,request,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer=EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer