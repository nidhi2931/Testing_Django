from django.contrib import admin
from .models import *

# Register your models here.

class NameAdmin(admin.ModelAdmin):
    list_display=('id','name')

admin.site.register(Name,NameAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display=('name','file')


admin.site.register(Document,DocumentAdmin)
