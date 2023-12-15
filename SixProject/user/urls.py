from django.urls import path
from .views import index, create, update, delete
urlpatterns = [
    path('', index, name='home'),
    path('create', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
