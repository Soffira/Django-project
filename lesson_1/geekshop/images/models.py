from django.db import models
# Create your models here.

class Image(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True
    )

    value = models.ImageField(
        upload_to='images/%Y/%m/%d/'
    )

    def __str__(self):
        return self.name