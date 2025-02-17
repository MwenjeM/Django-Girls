from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Define URL for homepage
]
