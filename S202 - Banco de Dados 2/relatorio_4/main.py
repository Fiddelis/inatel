from product_analyzer import ProductAnalyzer
from database import Database

db = Database(database="mercado", collection="compras")
# db.resetDatabase()

x = ProductAnalyzer(db)
x.get_total_vendas_dia()
x.get_produto_mais_vendido()
x.get_cliente_maior_compra()
x.get_produtos_vendidos_mais_que_uma_unidade()