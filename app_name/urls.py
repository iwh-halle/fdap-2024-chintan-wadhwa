from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('chart/', views.chart_view, name='chart_view'),  # Chart page
    path('deribit/', views.deribit_data, name='deribit_data'),  # API endpoint
]
