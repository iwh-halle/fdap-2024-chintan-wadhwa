from django.urls import path
from . import views

urlpatterns = [
    path('deribit/', views.deribit_data, name='deribit_data'),  # Define API endpoint
]
