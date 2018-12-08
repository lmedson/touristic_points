from rest_framework.viewsets import ModelViewSet
from avaliations.models import Avaliation
from .serializers import AvaliationSerializer


class AvaliationViewSet(ModelViewSet):

    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
