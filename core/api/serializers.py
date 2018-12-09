from rest_framework.serializers import ModelSerializer
from core.models import TouristAttraction


class TouristAttractionSerializer(ModelSerializer):
    class Meta:
        model = TouristAttraction
        fields = ['id', 'name', 'description', 'image']
