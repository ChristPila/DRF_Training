from django.core.management import BaseCommand
from django.db.models import Max, Count

from tracker.models import Chauffeur, Camions, Mouvements


class Command(BaseCommand):
    """def add_arguments(self, parser):
        parser.add_argument('camion_id', type=int)"""

    def handle(self, *args, **options):
        # rdvs = Mouvements.objects.filter(is_active=True).aggregate(max=Max('camion'))
        # mvt = rdvs['max']
        # b = Camions.objects.prefetch_related('mouvements_set').filter(is_active=True)
        # c = b.aggregate(max=Max('id'))
        """ca = Camions.objects.values()
        for key in ca:
            a = Mouvements.objects.select_related('camion').filter(camion=key['id'])
            b = a.count()
            print(f"Camion {key['id']} :", b)
        cb = Mouvements.objects.values('status').annotate(total=Count('status'))
        print(cb)"""
        ca = Mouvements.objects.values('date_created__date', 'status').annotate(rdv=Count('camion'))
        print(ca)

