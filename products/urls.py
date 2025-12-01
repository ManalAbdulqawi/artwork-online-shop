from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('add-to-watchlist/<int:product_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove-from-watchlist/<int:product_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
]