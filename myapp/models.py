from django.db import models

# Create your models here.
class Data(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Location = models.TextField(null=True)

    def __str__(self):
        return self.firstName