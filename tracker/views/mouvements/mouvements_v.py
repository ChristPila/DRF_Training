from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import Mouvements, Steps
from tracker.views.mouvements.mouvements_sz import MouvementSerializer, AddMouvementSerializer, \
    UpdateMouvementSerializer
from tracker.views.mouvementsDetails.mouvementD_sz import AddMouvementDSerializer


class EmptySZ(serializers.Serializer):
    pass


class MouvementViewSet(ModelViewSet):
    queryset = Mouvements.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['date_created']
    filterset_fields = ['is_active', 'date_created']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create_mvt':
            return AddMouvementSerializer
        methodes_list = dict(POST=EmptySZ, PUT=UpdateMouvementSerializer)
        return methodes_list.get(self.request.method, MouvementSerializer)

    @action(detail=False, methods=["POST"])
    def create_mvt(self, request):
        data = request.data
        sz = AddMouvementSerializer(data=data, context=dict(user=request.user))
        sz.is_valid(raise_exception=True)
        sz.save()
        mvt = sz.instance
        for step in Steps.objects.filter(is_active=True):
            data = dict(step=step.step, checkpoint=step.checkpoint)
            print('VUE:', data)
            print('MOUVEMENT: ', mvt)
            sz_d = AddMouvementDSerializer(data=data, context=dict(mouvements=mvt))
            sz_d.is_valid(raise_exception=True)
            sz_d.save()
        return Response('Mouvement crée avec succès !')



