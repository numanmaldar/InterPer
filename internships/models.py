from django.db import models
from django.db import models
from django.utils import timezone

class Internship(models.Model):
    internship_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    time_period = models.CharField(max_length=100)
    stipend = models.CharField(max_length=100)
    internship_link = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.internship_name} at {self.company_name}"