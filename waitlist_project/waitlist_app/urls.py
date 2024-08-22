from django.urls import path
from . import views

urlpatterns = [
    #Restaurant Paths
    path('', views.reshome, name='reshome'),
    path('add/', views.add_customer, name='add_customer'),
    path('all/', views.get_customers, name='get_customers')
]
