from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if '.csv' not in path:
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            return list(csv.DictReader(file))
