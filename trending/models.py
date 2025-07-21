from django.db import models

class TrendingRepo(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True)
    stars = models.IntegerField()
    language = models.CharField(max_length=100, blank=True)
    scraped_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.stars}⭐)"
