from rest_framework import routers
from .api import PostViewSet,CommentViewSet

routers = routers.DefaultRouter()

routers.register('api/post',PostViewSet,'post')
routers.register('api/comment',CommentViewSet,'comment')
urlpatterns=routers.urls