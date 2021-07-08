from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Interview(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name
