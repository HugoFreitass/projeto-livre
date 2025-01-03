from features.product import Product
import pickle
import os

class Stock:
    def __init__(self):
        self._file_name = 'stock.pkl'

    def load_stock(self):
        if os.path.exists(self._file_name):
            with open(self._file_name, 'rb') as file:
                return pickle.load(file)
        return []
    
    def save_stock(self, stock):
        with open(self._file_name, 'wb') as file:
            pickle.dump(stock, file)

    def register(self, product):
        if not isinstance(product, Product):
            raise ValueError("Formato inválido")

        stock = self.load_stock()
        stock.append(product)
        self.save_stock(stock)
        return f"Produto {product.name} registrado com sucesso"