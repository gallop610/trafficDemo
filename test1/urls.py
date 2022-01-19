from django.urls import path
from . import views

urlpatterns = [
    path('basic_test/', views.basic_test, name='basic_test'),
]