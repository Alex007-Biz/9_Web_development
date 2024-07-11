from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    review = models.TextField()
    class Meta:
        app_label = 'films'  # Specify the app label here