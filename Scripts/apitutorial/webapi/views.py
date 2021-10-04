# from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
# from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.


# With the help of API class getting Data in JSON Formate


class StudentList(APIView):

    def get(self, request):

        students = student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)


# With Decorator Passing Data to Get Function


@api_view(['GET'])
def studentdetails(request, pk):
    try:
        students = student.objects.get(id=pk)
        if students:
            serializer = StudentSerializers(students, many=False)
            return Response(serializer.data)
    except Exception as e:
        return Response("Error : {}".format(e))



# Adding New Data to Student with help of Decorator

@api_view(['POST'])
def studentadd(request):

    serializer = StudentSerializers(data=request.data)

    # Check Perticular Field of Post Data
    # print(request.data.get('fname'))

    if serializer.is_valid():
        serializer.save()
    return Response("Success!!")


# Updating Data Student With the help of Decorator

@api_view(['POST'])
def studentupdated(request, pk):

    updata = student.objects.get(id=pk)
    serializer = StudentSerializers(instance=updata, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Error While Updating Data!!")

    return Response("Data Updated Successfully!!")


# Deleting Data From Student with Decorator


@api_view(['POST'])
def studentdelete(request, pk):

    deletes = student.objects.get(id=pk)
    deletes.delete()

    return Response("Data Updated Successfully!!")


# Payment class with Helping Inherits APIViews class


class PaymentList(APIView):

    def get(self, request):

        payments = payment.objects.all()
        serializer = PaymentSerializers(payments, many=True)
        return Response(serializer.data)


