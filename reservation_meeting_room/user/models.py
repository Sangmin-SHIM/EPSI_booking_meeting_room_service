from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        unique_together = ["first_name", "last_name", "phone_number", "email"]

    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    department = models.ForeignKey(
        "department.Department", on_delete=models.CASCADE, null=False
    )

    def __str__(self):
        return f"{self.name} - {self.email}"
