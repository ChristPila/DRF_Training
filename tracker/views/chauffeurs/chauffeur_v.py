from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import Chauffeur
from tracker.views.chauffeurs.chauffeur_sz import ChauffeurSerializer, AddChauffeurSerializer


class ChauffeurViewset(ModelViewSet):
    serializer_class = ChauffeurSerializer
    http_method_names = ['get', 'put', 'patch']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = []
    filterset_fields = ['is_active', 'name']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddChauffeurSerializer
        return ChauffeurSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        query_set = Chauffeur.objects.all()
        return query_set
