from rest_framework import serializers
from .models import Name,Document


class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model=Name
        fields='__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields= ['id','name','file']


        
