from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(max_length=250)
    project_file = models.FileField(upload_to='zip/')
