from django.urls import path
from . import views


app_name = 'images'

urlpatterns = [
    path('', views.image_home, name='home'),
    path('images/create/', views.image_create, name='create'),
    path('images/detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('images/like/', views.image_like, name='like'),
    path('images/', views.image_list, name='list'),
]