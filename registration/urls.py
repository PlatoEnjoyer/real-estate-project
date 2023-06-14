from django.urls import path
from . import views


urlpatterns = [
    path('', views.registration),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.logout_user),
    path('profile/', views.profile),
]
