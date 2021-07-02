from rest_framework import routers
from .api import UserProfileViewSet

router = routers.DefaultRouter()
router.register('api/profiles', UserProfileViewSet, 'user_profiles')

urlpatterns = router.urls