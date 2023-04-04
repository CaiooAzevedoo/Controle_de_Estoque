from inventory_report.inventory.product import Product
import datetime


def test_cria_produto():
    product = Product(1, 'empresa', 'produto', datetime.date(2023, 4, 4),
                      datetime.date(2024, 4, 4), 321, 'guardar')

    assert product.id == 1
    assert product.nome_do_produto == 'empresa'
    assert product.nome_da_empresa == 'produto'
    assert product.data_de_fabricacao == '2023-04-04'
    assert product.data_de_validade == '2024-04-04'
    assert product.numero_de_serie == 321
    assert product.instrucoes_de_armazenamento == 'guardar'
