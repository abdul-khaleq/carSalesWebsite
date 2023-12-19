from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddCarCreateView.as_view(), name='add_car'),
    path('buy_now/<int:id>', views.orderHistory, name='buy_now'),
    path('detail/<int:id>', views.CarDetailView.as_view(), name='car_details'),
]