from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "produto",
        "empresa",
        "2023-04-04",
        "2024-04-04",
        "321",
        "guardar",
    )

    message = """O produto produto fabricado em \
2023-04-04 por empresa com \
validade até 2024-04-04 precisa ser \
armazenado guardar."""

    assert str(product) == message
