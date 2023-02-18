from rest_framework.serializers import ModelSerializer

from tracker.models import MouvementDetails


class MouvementDSerializer(ModelSerializer):
    class Meta:
        model = MouvementDetails
        fields = '__all__'


class AddMouvementDSerializer(ModelSerializer):
    class Meta:
        model = MouvementDetails
        fields = ['mouvements', 'id']
