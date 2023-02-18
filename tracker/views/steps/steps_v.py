from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import status

from tracker.models import Steps
from tracker.views.steps.steps_sz import StepsSerializer, AddStepsSerializer, DisableStepsSerializer


class StepsViewset(ModelViewSet):
    serializer_class = StepsSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_serializer_class(self):
        if self.action == "desctivate_steps":
            return DisableStepsSerializer
        if self.request.method == 'POST':
            return AddStepsSerializer
        """if self.request.method == 'PUT':
            return UpdateCategorySerializer"""
        return StepsSerializer

    def get_queryset(self):
        return Steps.objects.all()

    @action(detail=False, methods=["post"])
    def desctivate_steps(self, request):
        Steps.objects.filter(is_active=True).update(is_active=False)
        return Response("operation terminée !", status=status.HTTP_200_OK)
