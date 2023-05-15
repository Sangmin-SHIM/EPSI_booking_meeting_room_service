from django.contrib import admin
from .models import Reservation

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'start_datetime','end_datetime','comment','user')
    search_fields = ('name', 'room', 'start_datetime','end_datetime','comment','user')