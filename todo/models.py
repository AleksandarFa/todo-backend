from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)

    LOW = "LOW"
    MED = "MED"
    HIGH = "HIGH"

    PRIORITY_CHOICES = [(LOW, "Low"), (MED, "Medium"), (HIGH, "High"), ]

    priority_choice = models.CharField(
        max_length=4, choices=PRIORITY_CHOICES, default=LOW)

    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="user",
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
