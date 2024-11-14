from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    academy = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    certificate_image = models.ImageField(upload_to='images/')

