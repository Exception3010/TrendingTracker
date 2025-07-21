from rest_framework import serializers
from .models import TrendingRepo

class TrendingRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingRepo
        fields = ['id', 'name', 'url', 'description', 'stars', 'language', 'scraped_date']
