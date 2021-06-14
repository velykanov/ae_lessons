from django.db import models


class Actor(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
