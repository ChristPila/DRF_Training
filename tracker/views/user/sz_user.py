from django.db.models import Q
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth import get_user_model
from tracker.models import Mouvements, Camions, Chauffeur


class UserInfosSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']