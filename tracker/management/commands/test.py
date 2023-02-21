from django.core.management import BaseCommand
from tracker.models import Chauffeur

class Command(BaseCommand):
    def chauffeur(self):
        q = Chauffeur.objects.values()
        for data in q:
            print(data)
        #def handle(self, *args, **options):