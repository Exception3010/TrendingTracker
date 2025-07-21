from rest_framework.routers import DefaultRouter
from .views import TrendingRepoViewSet

router = DefaultRouter()
router.register(r'trending', TrendingRepoViewSet, basename='trending')

urlpatterns = router.urls
