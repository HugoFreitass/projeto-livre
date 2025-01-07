from packages.product import Product
from packages.stock import Stock
from packages.sales import Sales

class ManagementSystem(Stock):
    def __init__(self):
        self.file_name  = 'stock.pkl'
        self._sales = []
    
    def new_sale(self) -> Sales:
        sale = Sales(self)
        self._sales.append(sale)
        return sale
    
    def register_product(self, barcode, name, price, amount) -> str:
        product = Product(barcode, name, price, amount)
        return super().register_product(product)