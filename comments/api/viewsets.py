from rest_framework.viewsets import ModelViewSet
from core.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
