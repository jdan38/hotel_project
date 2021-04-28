from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hotels'),
    path('<int:hotel_id>', views.hotel, name='hotel'),
   
]