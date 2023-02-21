from django.db.models import Q
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, ValidationError

from tracker.models import Mouvements, Camions, Chauffeur


class MouvementSerializer(ModelSerializer):
    user_name = SerializerMethodField()

    class Meta:
        model = Mouvements
        fields = '__all__'

    def get_user_name(self, obj):
        user = obj.user
        print('UTILISATEURS:', user)
        if user:
            return user.username
        return ""


class AddMouvementSerializer(ModelSerializer):
    camion = PrimaryKeyRelatedField(queryset=Camions.objects.filter(is_active=True))

    class Meta:
        model = Mouvements
        fields = ['id', 'date_created', 'remote_id', 'camion', 'chauffeurs']

    def validate(self, data):
        remote = data['remote_id']
        q = Mouvements.objects.filter(remote_id=remote)
        if q.filter(~Q(status="1")).exists():
            raise ValidationError(detail="Le RDV existe deja")
        else:
            q.delete()
        print('validate', data)
        data['user'] = self.context['user']
        return super().validate(data)


class UpdateMouvementSerializer(ModelSerializer):
    chauffeurs = PrimaryKeyRelatedField(queryset=Chauffeur.objects.filter(is_active=True))

    class Meta:
        model = Mouvements
        fields = ['is_active', 'chauffeurs']

    def validate(self, data):
        data['status'] = "2"
        print('validate', data)
        return super().validate(data)
