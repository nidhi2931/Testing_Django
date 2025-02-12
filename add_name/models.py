from django.db import models

# Create your models here.


class Name(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.name}"


class Document(models.Model):
    name=models.ForeignKey(Name,on_delete=models.CASCADE,related_name='documents')
    file=models.FileField(upload_to='documents/')

    def __str__(self):
        return f"Documents for {self.name.name}"
