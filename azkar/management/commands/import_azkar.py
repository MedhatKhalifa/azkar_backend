import pandas as pd
from django.core.management.base import BaseCommand
from azkar.models import Azkar
# python manage.py import_azkar azkar/management/commands/azkar_all.xlsx
class Command(BaseCommand):
    help = "Import Azkar from Excel or CSV"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the Excel or CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            # Read file into a DataFrame
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                self.stderr.write("Unsupported file format. Use .csv or .xlsx.")
                return

            # Iterate over rows and create Azkar entries
            for _, row in df.iterrows():
                Azkar.objects.create(
                    category=row.get('category'),
                    sub_category=row.get('sub_category'),
                    content=row.get('content'),
                    before=row.get('before'),
                    after=row.get('after'),
                    count=row.get('count', 1),
                    reward=row.get('reward'),
                    when=row.get('when'),
                    where=row.get('where'),
                    why=row.get('why'),
                    source=row.get('source'),
                    comment=row.get('comment'),
                    language=row.get('language', 'ar'),
                    icon_name=row.get('icon_name'),
                )
            self.stdout.write("Data imported successfully.")
        except Exception as e:
            self.stderr.write(f"Error importing data: {e}")
