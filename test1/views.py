from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer


# Create your views here.

class FileUploadView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            files=serializer.save()
            return Response({"message":"Files Uploaded Successfully.","files":[file.files.url for file in files]},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)