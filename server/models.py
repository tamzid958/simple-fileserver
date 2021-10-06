from django.db import models


# Create your models here.
class FileServer(models.Model):
    file = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.file
