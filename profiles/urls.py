from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("orders_list/", views.orders_list, name="orders_list"),
    path("order_history/<order_number>", views.order_history,
         name="order_history"),
]
