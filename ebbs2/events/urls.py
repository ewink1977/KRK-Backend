from rest_framework import routers, urlpatterns
from .api import EventViewSet

router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')

urlpatterns = router.urls