from django.urls import path
from .views import create_assistant

urlpatterns = [
    path('create/', create_assistant, name='create_assistant'),
]
