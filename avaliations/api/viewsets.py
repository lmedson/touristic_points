from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from avaliations.models import Avaliation
from .serializers import AvaliationSerializer


class AvaliationViewSet(ModelViewSet):

    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nota', 'data', 'user')
