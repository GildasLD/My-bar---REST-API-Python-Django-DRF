from rest_framework.routers import DefaultRouter
 
from beers.views import BarsViewSet, ReferenceViewSet, StockViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
 

router.register(r'references', ReferenceViewSet, basename='references')
router.register(r'bars', BarsViewSet, basename='bars')
router.register(r'stocks', StockViewSet, basename='stocks')
 
urlpatterns = router.urls
 