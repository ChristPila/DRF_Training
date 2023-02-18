from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import MouvementDetails
from tracker.views.mouvementsDetails.mouvementD_sz import MouvementDSerializer, AddMouvementDSerializer


class MouvDViewset(ModelViewSet):
    serializer_class = MouvementDSerializer
    http_method_names = ['get', 'post' 'put', 'patch']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddMouvementDSerializer
        return MouvementDSerializer

    def get_queryset(self):
        query_set = MouvementDetails.objects.all()
        return query_set
