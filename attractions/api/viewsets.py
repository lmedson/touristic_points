from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from attractions.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):

    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'description', 'min_age')
