from . import views
from django.urls import path

app_name = "user"  # namespace

urlpatterns = [path("create", views.create_user, name="create_user")]
