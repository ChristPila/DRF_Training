from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracker.views.camions.camions_v import CamionViewset
from tracker.views.chauffeurs.chauffeur_v import ChauffeurViewset
from tracker.views.mouvements.mouvements_v import MouvementViewSet
from tracker.views.mouvementsDetails.mouvD_v import MouvDViewset
from tracker.views.steps.steps_v import StepsViewset

# Ici nous créons notre routeur
router = routers.DefaultRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre views
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('camions', CamionViewset, basename='camions')
router.register('chauffeurs', ChauffeurViewset, basename='chauffeurs')
router.register('mouvements', MouvementViewSet, basename='mouvements')
router.register('mouvements-details', MouvDViewset, basename='mouvements-details')
router.register('steps', StepsViewset, basename='steps')

urlpatterns = [
    path('api/', include(router.urls))
]