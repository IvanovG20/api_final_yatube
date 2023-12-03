from rest_framework import routers

from django.urls import path, include

from api.views import (PostViewSet, CommentViewSet,
                       GroupViewSet, FollowViewSet)


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
