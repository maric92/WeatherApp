from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __set__(self):
        return self.name
