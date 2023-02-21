from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from tracker.models import Camions
from tracker.views.camions.camions_sz import CamionSerializer, AddCamionSerializer


class CamionViewset(ModelViewSet):
    serializer_class = CamionSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCamionSerializer
        return CamionSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        query_set = Camions.objects.all()
        return query_set
