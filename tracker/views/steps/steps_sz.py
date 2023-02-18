from rest_framework.serializers import ModelSerializer, ValidationError
from django.db.models import Max
from tracker.models import Steps


class StepsSerializer(ModelSerializer):
    class Meta:
        model = Steps
        fields = '__all__'


class AddStepsSerializer(ModelSerializer):
    class Meta:
        model = Steps
        fields = ['id', 'checkpoint']

    def validate(self, data):
        ag = Steps.objects.filter(is_active=True).aggregate(max=Max('step'))
        step = ag['max'] or 0
        q = Steps.objects.filter(step=step + 1, is_active=True)
        if q.exists():
            raise ValidationError(detail=f"L'étape {step + 1} existe déjà")
        data['step'] = step + 1
        return super().validate(data)


class UpdateStepsSerializer(ModelSerializer):
    class Meta:
        model = Steps
        fields = ['id', 'checkpoint']


class DisableStepsSerializer(ModelSerializer):
    class Meta:
        model = Steps
        fields = []
