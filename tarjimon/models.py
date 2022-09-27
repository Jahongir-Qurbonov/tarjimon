from django.db import models


class Lugat(models.Model):

    inglizcha = models.CharField(max_length=128)
    uzbekcha = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.inglizcha} - {self.uzbekcha}"