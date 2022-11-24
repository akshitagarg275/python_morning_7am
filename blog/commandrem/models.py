from django.db import models

# Create your models here.
class CommandRem(models.Model):
    cmd = models.CharField(max_length=500)

    def __str__(self):
        return self.cmd