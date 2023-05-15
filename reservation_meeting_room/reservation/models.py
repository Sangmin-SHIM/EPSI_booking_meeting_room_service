from django.db import models

# Create your models here.

class Reservation(models.Model):
    class Meta:
        unique_together = ['room', 'start_datetime','end_datetime']
    name = models.CharField(max_length=50,unique=True)
    room = models.ForeignKey("room.Room", on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.room} - {self.start_datetime} - {self.end_datetime} - {self.comment} - {self.user}"