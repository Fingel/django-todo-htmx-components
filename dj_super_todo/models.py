from django.db import models


class Todo(models.Model):
    done = models.BooleanField(blank=True, default=False)
    content = models.CharField(max_length=500)
