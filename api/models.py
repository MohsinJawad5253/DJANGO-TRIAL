from django.db import models

# Create your models here.
class Doctors(models.Model):
    doctor_id=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    field=models.CharField(max_length=50)

    def __str__(self):
        return self.name