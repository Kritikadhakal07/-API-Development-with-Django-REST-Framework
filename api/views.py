from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#Here we were manually serailizing the query set by converting them in list and
#returning it as json response

# def studentsView(request):
#    students=Student.objects.all()
#    student_list = list(students.values())
#    return JsonResponse(student_list,safe=False)


@api_view(['GET','POST'])
def studentsView(request):
   #  print(request)
    """
    This view function handles the HTTP GET request to get all the data
    from the student table. It returns a JSON response containing the serialized
    data.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response object containing the serialized data.
    """

    if request.method == 'GET':
        #Get all the data from the student table
        students=Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #Create a new student(Post)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student=Student.objects.get(pk=pk)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)