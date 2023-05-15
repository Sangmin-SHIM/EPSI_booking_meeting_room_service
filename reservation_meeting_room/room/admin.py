from django.contrib import admin
from .models import Room

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'room_number','available','capacity','equipment')
    search_fields = ('name', 'floor', 'room_number','available','capacity','equipment')