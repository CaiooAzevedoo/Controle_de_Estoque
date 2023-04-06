from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if '.json' not in path:
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            return list(json.load(file))
