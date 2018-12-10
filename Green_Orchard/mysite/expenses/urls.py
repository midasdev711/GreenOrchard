from django.urls import path
from . import views

app_name = 'expenses'
urlpatterns = [
    path('', views.index, name='index'),
    path('month/', views.month, name='month'),
    path('summary/', views.summary, name='summary'),
    path('category/', views.category, name='category'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('faq/', views.faq, name='faq')
]
