from django.urls import path
from . import views


app_name = 'hello_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

