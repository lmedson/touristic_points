from rest_framework.serializers import ModelSerializer
from avaliations.models import Avaliation


class AvaliationSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = ['id', 'user', 'comment', 'nota',
                  'data']
