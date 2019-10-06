from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=20, default=None)
    sound = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.name
