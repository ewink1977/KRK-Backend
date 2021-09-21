from rest_framework import routers
from .api import AllPostViewSet, AllReplyViewSet, AddPostViewSet, SinglePostViewSet

router = routers.DefaultRouter()
router.register('api/posts', AllPostViewSet, 'posts'),
router.register('api/posts/<id>', SinglePostViewSet, 'posts'),
router.register('api/replies', AllReplyViewSet, 'replies'),
router.register('api/addpost', AddPostViewSet, 'addpost'),

urlpatterns = router.urls