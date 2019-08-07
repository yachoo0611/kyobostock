from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:isbn>/result/', views.result, name='result'),
    path('select/', views.select, name='select')
]