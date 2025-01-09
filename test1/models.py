from django.db import models

# Create your models here.


class FilesModel(models.Model):
    files=models.FileField(upload_to='uploads/documents/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"File:{self.files.name}"

    
