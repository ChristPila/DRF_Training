from rest_framework.serializers import ModelSerializer

from tracker.models import Chauffeur


class ChauffeurSerializer(ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = '__all__'
