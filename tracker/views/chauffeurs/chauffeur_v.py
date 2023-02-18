from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import Chauffeur
from tracker.views.chauffeurs.chauffeur_sz import ChauffeurSerializer


class ChauffeurViewset(ModelViewSet):
    serializer_class = ChauffeurSerializer

    def get_queryset(self):
        query_set = Chauffeur.objects.all()
        return query_set
