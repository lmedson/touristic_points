from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from adresses.models import Adress
from .serializers import AdressSerializer


class AdressViewSet(ModelViewSet):

    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('city', 'state', 'country')
