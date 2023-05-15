from django.db import models

# Create your models here.


class Room(models.Model):
    class Meta:
        unique_together = ["floor", "room_number"]

    name = models.CharField(max_length=50, unique=True)
    floor = models.IntegerField()
    room_number = models.IntegerField()
    available = models.BooleanField(default=True)
    capacity = models.IntegerField()
    equipment = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return f"{self.name} - {self.room_number}"
