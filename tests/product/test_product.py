from inventory_report.inventory.product import Product
import datetime


def test_cria_produto():
    product = Product(
        id=1,
        nome_da_empresa='empresa',
        nome_do_produto='produto',
        data_de_fabricacao=datetime.date(2023, 4, 4),
        data_de_validade=datetime.date(2024, 4, 4),
        numero_de_serie=321,
        instrucoes_de_armazenamento='guardar')

    assert product.id == 1
    assert product.nome_do_produto == 'produto'
    assert product.nome_da_empresa == 'empresa'
    assert product.data_de_fabricacao == '2023-04-04'
    assert product.data_de_validade == '2024-04-04'
    assert product.numero_de_serie == 321
    assert product.instrucoes_de_armazenamento == 'guardar'
