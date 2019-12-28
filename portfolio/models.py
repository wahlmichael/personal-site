from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_live = models.BooleanField(default=False)
    github_link = models.CharField(max_length=200)
    live_link = models.CharField(max_length=200)
    def __str__(self):
        return self.name

