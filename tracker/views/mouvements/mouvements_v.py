from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import Mouvements
from tracker.views.mouvements.mouvements_sz import MouvementSerializer, AddMouvementSerializer, \
    UpdateMouvementSerializer


class MouvementViewSet(ModelViewSet):
    queryset = Mouvements.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['date_created']
    filterset_fields = ['is_active', 'date_created']

    def get_serializer_class(self):
        methodes_list = dict(POST=AddMouvementSerializer, PUT=UpdateMouvementSerializer)
        return methodes_list.get(self.request.method, MouvementSerializer)
