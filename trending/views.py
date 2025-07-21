from rest_framework import viewsets
from .models import TrendingRepo
from .serializers import TrendingRepoSerializer

class TrendingRepoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrendingRepo.objects.all().order_by('-scraped_date', '-stars')
    serializer_class = TrendingRepoSerializer
