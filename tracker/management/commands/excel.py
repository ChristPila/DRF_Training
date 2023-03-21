from django.core.management import BaseCommand
from django.db.models import Max, Count
import xlsxwriter
from tracker.models import Camions


class Command(BaseCommand):
    def handle(self, *args, **options):
        workbook = xlsxwriter.Workbook("excel_template.xlsx")
        worksheet = workbook.add_worksheet("firstsheet")

        worksheet.write(0, 0, "Id")
        worksheet.write(0, 1, "Nom")

        camions = Camions.objects.values('id', 'name')
        print("Camions : ",camions)

        for index, entry in enumerate(camions):
            worksheet.write(index+1, 0, entry['id'])
            worksheet.write(index+1, 1, entry['name'])
        workbook.close()
