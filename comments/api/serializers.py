from rest_framework.serializers import ModelSerializer
from core.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'data', 'approved']
