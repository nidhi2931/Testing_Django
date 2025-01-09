from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.username


