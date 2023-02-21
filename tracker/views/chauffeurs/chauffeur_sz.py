from rest_framework.serializers import ModelSerializer

from tracker.models import Chauffeur


class ChauffeurSerializer(ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = '__all__'


class AddChauffeurSerializer(ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = ['name', 'is_active']

    def validate(self, data):
        data['user'] = self.context['user']
        return super().validate(data)
