from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        data = Inventory.read_file(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)

    @staticmethod
    def read_file(path):
        if '.csv' in path:
            return CsvImporter.import_data(path)
        elif '.json' in path:
            return JsonImporter.import_data(path)
        elif '.xml' in path:
            return XmlImporter.import_data(path)
