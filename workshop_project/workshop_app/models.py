from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return self.name
