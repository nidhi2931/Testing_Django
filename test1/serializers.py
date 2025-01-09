from rest_framework import serializers
from .models import FilesModel

class FileUploadSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )

    def create(self, validated_data):
        files = validated_data.get('files', [])
        instances = []
        for file in files:
            instance = FilesModel.objects.create(files=file)  # Use `files` as the keyword argument
            instances.append(instance)
        return instances
