from django.contrib import admin
from .models import *

# Register your models here.

class FileModelAdmin(admin.ModelAdmin):
    list_display=('id','files')

admin.site.register(FilesModel,FileModelAdmin)


