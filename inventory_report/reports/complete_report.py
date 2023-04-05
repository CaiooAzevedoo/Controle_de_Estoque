from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(inventory_list):
        inventory_products = dict()
        for product in inventory_list:
            if product["nome_da_empresa"] not in inventory_products:
                inventory_products[product["nome_da_empresa"]] = 1
            else:
                inventory_products[product["nome_da_empresa"]] += 1

        inventory_products_sorted = sorted(inventory_products.items())

        result = (
                f"{SimpleReport.generate(inventory_list)}\n"
                f"Produtos estocados por empresa:\n"
            )
        for company, quantity in inventory_products_sorted:
            result += f"- {company}: {quantity}\n"

        return result
