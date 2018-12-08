from rest_framework.viewsets import ModelViewSet
from core.models import Adress
from .serializers import AdressSerializer


class AdressViewSet(ModelViewSet):

    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
