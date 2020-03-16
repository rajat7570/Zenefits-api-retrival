from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_w, name='list_w'),
    path('emp/<int:id>/', views.emp_detail, name='emp_detail'),
]