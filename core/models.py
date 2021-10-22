from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='poster')

    def __str__(self):
        return self.title