from django.db import models
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Добавьте другие поля, если необходимо

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])
