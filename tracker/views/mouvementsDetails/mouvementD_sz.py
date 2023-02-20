from django.db.models import Max
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from tracker.models import MouvementDetails


class MouvementDSerializer(ModelSerializer):
    class Meta:
        model = MouvementDetails
        fields = '__all__'

    def validate(self, data):
        ag = MouvementDetails.objects.filter(is_active=True).aggregate(max=Max('step'))
        step = ag['max'] or 0
        q = MouvementDetails.objects.filter(step=step + 1, is_active=True)
        if q.exists():
            raise ValidationError(detail=f"L'étape {step + 1} existe déjà")
        data['step'] = step + 1
        return super().validate(data)


class AddMouvementDSerializer(ModelSerializer):
    class Meta:
        model = MouvementDetails
        fields = ['step', 'checkpoint']

    def validate(self, data):
        data['mouvements'] = self.context['mouvements']
        print('Les donnees :', data)
        return super().validate(data)


class NextStepsSerializer(ModelSerializer):
    class Meta:
        model = MouvementDetails
        fields = []
