from rest_framework.serializers import ModelSerializer
from adresses.models import Adress


class AdressSerializer(ModelSerializer):
    class Meta:
        model = Adress
        fields = ['id', 'line_adress1', 'city', 'state',
                  'country', 'latitude', 'longitude']
