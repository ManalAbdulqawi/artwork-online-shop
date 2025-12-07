from . import views
from django.urls import path

urlpatterns = [
    path("", views.enquiry_us, name="enquiry"),
]
