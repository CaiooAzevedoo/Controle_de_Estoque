from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if '.xml' not in path:
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            tree = ET.parse(file)
            dataset = tree.getroot()

        invetory_list = list()
        for product in dataset:
            invetory_dict = dict()
            for item in product:
                invetory_dict[item.tag] = item.text
            invetory_list.append(invetory_dict)

        return invetory_list
