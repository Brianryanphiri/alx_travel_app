from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint (you can add actual API views here later)
    path('', views.home, name='home'),
]
