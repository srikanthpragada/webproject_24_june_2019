from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from django.shortcuts import render


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'fullname', 'email', 'course', 'feepaid')


def client(request):
    return render(request, "rest_client.html")


@api_view(['GET', 'POST'])
def students_get_post(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    else:  # POST
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Insert
            return Response(serializer.data)
        else:  # Error
            return Response(serializer.errors, status=400)


@api_view(['DELETE', 'GET'])
def process_one_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except:
        return Response(status=404)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    else:  # DELETE
        student.delete()
        return Response(status=204)  # No content
