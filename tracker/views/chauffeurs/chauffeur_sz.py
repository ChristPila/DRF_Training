from rest_framework.serializers import ModelSerializer

from tracker.models import Chauffeur
from tracker.views.user.sz_user import UserInfosSerializer


class ChauffeurSerializer(ModelSerializer):
    user = UserInfosSerializer()

    class Meta:
        model = Chauffeur
        fields = '__all__'


class ChauffeursInfos(ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = ['id', 'name']


class AddChauffeurSerializer(ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = ['name', 'is_active']

    def validate(self, data):
        data['user'] = self.context['user']
        return super().validate(data)
