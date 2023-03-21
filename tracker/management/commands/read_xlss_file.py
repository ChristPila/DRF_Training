from django.core.management import BaseCommand
from django.db.models import Max, Count
import pandas as pd
from tracker.views.camions.camions_sz import CamionSerializer, AddCamionSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        df = pd.read_excel("excel_template.xlsx")
        #data = pd.DataFrame(workbook, columns=['Nom'])
        print("Le contenu du fichier est :", df)
        """print("Le contenu du fichier est :", df.to_dict("records"))
        tb = df.to_dict("records")

        for n in tb:
            sz = AddCamionSerializer(data=n)
            sz.is_valid()
        sz.save()"""

