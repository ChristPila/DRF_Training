from django.urls import path, include
from rest_framework import routers

from tracker.views.camions.camions_v import CamionViewset
from tracker.views.chauffeurs.chauffeur_v import ChauffeurViewset
from tracker.views.mouvements.mouvements_v import MouvementViewSet
from tracker.views.mouvementsDetails.mouvD_v import MouvDViewset
from tracker.views.steps.steps_v import StepsViewset

router = routers.DefaultRouter()
router.register('camions', CamionViewset, basename='camions')
router.register('chauffeurs', ChauffeurViewset, basename='chauffeurs')
router.register('mouvements', MouvementViewSet, basename='mouvements')
router.register('mouvements-details', MouvDViewset, basename='mouvements-details')
router.register('steps', StepsViewset, basename='steps')

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #path('auth/', include('djoser.urls.authtoken')),
]