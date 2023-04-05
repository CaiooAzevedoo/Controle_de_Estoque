from datetime import date, datetime


class SimpleReport:
    def generate(products):
        atual = date.today()
        frabicacao = sorted(
            [data["data_de_fabricacao"] for data in products])[0]
        validades = [
            data["data_de_validade"] for data in products
            if datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
            > atual]
        validades = sorted(validades)[0]
        empresas = [nome["nome_da_empresa"] for nome in products]
        empresa_com_mais_produtos = max(set(empresas), key=empresas.count)

        result = (
            f"Data de fabricação mais antiga: {frabicacao}"
            f"Data de validade mais próxima: {validades}"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )
        
        return result
