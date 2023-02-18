from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from tracker.models import Camions
from tracker.views.camions.camions_sz import CamionSerializer


class CamionViewset(ModelViewSet):
    serializer_class = CamionSerializer

    def get_queryset(self):
        query_set = Camions.objects.all()
        return query_set
