from django.db import models

class Files(models.Model):
    # Defina seus campos aqui
    pass

class Trainings(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_link = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    