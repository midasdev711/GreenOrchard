from django.urls import path
from . import views

app_name = 'expenses'
urlpatterns = [
    path('', views.index, name='index'),
    path('month/', views.month, name='month'), # Change month to 201801
    path('summary/', views.summary, name='expense-summary'),
    path('category/', views.category, name='category'),
]
