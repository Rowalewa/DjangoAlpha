from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.CharField(max_length=100)

    def __str__(self):
        return self.username
