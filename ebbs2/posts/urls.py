from rest_framework import routers
from django.urls import path, include

# from posts.views import TestView
# from .api import AllPostViewSet, AllReplyViewSet, SinglePostViewSet
from .views import AddPostAPI, AllPosts

# router = routers.DefaultRouter()
# router.register('api/posts', AllPostViewSet, 'posts')
# router.register('api/posts/<id>', SinglePostViewSet, 'single_post')
# router.register('api/replies', AllReplyViewSet, 'replies')
# router.register('api/add_post', AddPostAPI, 'addpost')

# urlpatterns = router.urls
urlpatterns = [
    path('api/posts', AllPosts.as_view(), name='all_posts'),
    path('api/add_post/', AddPostAPI.as_view(), name='add_post'),
]
