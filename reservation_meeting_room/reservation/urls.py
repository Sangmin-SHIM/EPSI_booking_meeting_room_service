from . import views
from django.urls import path


app_name = "reservation"  # namespace

urlpatterns = [path("", views.create_reservation, name="create_reservation")]
