from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('add/', add, name='add'),
    path('edit/<int:id>/', news_edit, name='news_edit'),
    path('delete/<int:id>/', news_delete, name='news_delete'),
    path('', index, name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)