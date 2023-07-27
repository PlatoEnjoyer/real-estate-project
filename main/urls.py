from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_view, name='home'),
    path('calculate/', views.calculate_apartment_price, name='calculate_apartment_price'),
    path('input_params/', views.input_apart_params),
    path('about/', views.about_view)
]
