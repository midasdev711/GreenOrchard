from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'), # Change month to 201801
]
