from rest_framework import routers
from .api import AllPostViewSet, AllReplyViewSet

router = routers.DefaultRouter()
router.register('api/posts', AllPostViewSet, 'posts'),
router.register('api/replies', AllReplyViewSet, 'replies'),

urlpatterns = router.urls