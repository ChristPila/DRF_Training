from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tracker.models import MouvementDetails
from tracker.views.mouvementsDetails.mouvementD_sz import MouvementDSerializer, AddMouvementDSerializer, \
    NextStepsSerializer


class MouvDViewset(ModelViewSet):
    serializer_class = MouvementDSerializer
    http_method_names = ['get', 'put', 'patch']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = []
    filterset_fields = ['is_active', 'mouvements']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """if self.action == 'next':
            return NextStepsSerializer"""
        if self.request.method == 'POST':
            return AddMouvementDSerializer
        return MouvementDSerializer

    def get_queryset(self):
        return MouvementDetails.objects.all()

    """"@action(detail=False, methods=["post", "get"])
    def next(self, request):
        MouvementDetails.objects.filter(is_active=True).update(is_active=False)
        return Response("Étape suivante !", status=status.HTTP_200_OK)"""
