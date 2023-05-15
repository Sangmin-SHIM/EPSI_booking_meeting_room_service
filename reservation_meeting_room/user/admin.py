from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "password",
        "first_name",
        "last_name",
        "phone_number",
        "department",
    )
    search_fields = (
        "email",
        "password",
        "first_name",
        "last_name",
        "phone_number",
        "department",
    )
