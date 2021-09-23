from rest_framework import routers
from .api import AllAuthorData, UserProfileViewSet, PostAuthorData

router = routers.DefaultRouter()
router.register('api/profiles', UserProfileViewSet, 'user_profiles')
router.register('api/postauthor/<id>', PostAuthorData, 'post_author')
router.register('api/postauthor', AllAuthorData, 'all_author_data')

urlpatterns = router.urls