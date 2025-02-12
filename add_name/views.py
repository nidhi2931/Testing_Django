from django.shortcuts import render
from rest_framework import generics

from .models import Name, Document
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class NameListCreateView(generics.ListCreateAPIView):
    queryset=Name.objects.all()
    serializer_class=NameSerializer

class NameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Name.objects.all()
    serializer_class=NameSerializer



class UploadDocsView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            for key in request.FILES.keys():
                    if key.startswith('files_'):
                        name_id=int(key.split('_')[1])
                        name=Name.objects.get(id=name_id)
                        files=request.FILES.getlist(key)
                        for file in files:
                            Document.objects.create(name=name,file=file)
            return Response({"message":"Files uploaded successfully"},status=status.HTTP_201_CREATED)
        except Name.DoesNotExist:
            return Response({"error":"Name not found"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

    







