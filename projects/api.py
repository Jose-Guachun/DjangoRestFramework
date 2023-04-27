from .models import Post,Comment
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all().order_by('-id')
    permission_classes=[permissions.AllowAny]
    serializer_class=PostSerializer

    @action(detail=False, methods=['post'])
    def guardar(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CommentSerializer