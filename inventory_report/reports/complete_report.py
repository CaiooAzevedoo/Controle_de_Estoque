from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(inventory_list):
        inventory_products = dict()
        for product in inventory_list:
            if product["nome_da_empresa"] not in inventory_products:
                inventory_products[product["nome_da_empresa"]] = 1
            else:
                inventory_products[product["nome_da_empresa"]] += 1
