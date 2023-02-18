from rest_framework.serializers import ModelSerializer

from tracker.models import Camions


class CamionSerializer(ModelSerializer):
    class Meta:
        model = Camions
        fields = '__all__'
