from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields=('id', 'username','location','avatar','photo','like','bookmark','postComment','create_at')
        read_only_fields = ('create_at',)
