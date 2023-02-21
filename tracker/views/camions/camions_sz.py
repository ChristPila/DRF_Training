from rest_framework.serializers import ModelSerializer

from tracker.models import Camions


class CamionSerializer(ModelSerializer):
    class Meta:
        model = Camions
        fields = '__all__'


class CamionsInfos(ModelSerializer):
    class Meta:
        model = Camions
        fields = ['id', 'name']


class AddCamionSerializer(ModelSerializer):
    class Meta:
        model = Camions
        fields = ['name', 'is_active']

    def validate(self, data):
        data['user'] = self.context['user']
        return super().validate(data)
