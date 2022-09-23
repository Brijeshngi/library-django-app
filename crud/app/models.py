from django.db import models

class bookDetails(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)


