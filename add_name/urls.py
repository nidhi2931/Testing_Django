from django.urls import path
from .views import *

urlpatterns=[
    path('names/',NameListCreateView.as_view(),name='name-list-create'),
    path('names/<int:pk>/',NameRetrieveUpdateDestroyView.as_view(),name='name-detail'),
    path('upload_docs/',UploadDocsView.as_view(),name='upload_docs'),
    
]