# urls.py

from django.urls import path
from .views import connect_polygon

urlpatterns = [
    path('api/connect', connect_polygon, name='connect_polygon'),
]
