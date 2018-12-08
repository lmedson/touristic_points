from rest_framework.viewsets import ModelViewSet
from adresses.models import Adress
from .serializers import AdressSerializer


class AdressViewSet(ModelViewSet):

    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
