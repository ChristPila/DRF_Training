from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import Chauffeur
from tracker.views.chauffeurs.chauffeur_sz import ChauffeurSerializer, AddChauffeurSerializer


class ChauffeurViewset(ModelViewSet):
    serializer_class = ChauffeurSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddChauffeurSerializer
        return ChauffeurSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        query_set = Chauffeur.objects.all()
        return query_set
