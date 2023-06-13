from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_view),
    path('calculate/', views.calculate_apartment_price, name='calculate_apartment_price'),
    path('input_params/', views.input_apart_params),
]
