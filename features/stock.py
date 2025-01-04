from features.product import Product
import pickle
import os

class Stock:
    current_position = 0

    def __init__(self):
        self._file_name = 'stock.pkl'
        #self._products_position = {}

    def load_stock(self):#abstract
        if os.path.exists(self._file_name):
            with open(self._file_name, 'rb') as file:
                return pickle.load(file)
        return []
    
    def save_stock(self, stock):#abstract
        with open(self._file_name, 'wb') as file:
            pickle.dump(stock, file)

    def register(self, product):
        if not isinstance(product, Product):
            raise ValueError("Formato inválido")

        stock = self.load_stock()
        product.position = Stock.current_position
        stock.append(product)
        Stock.current_position += 1
        self.save_stock(stock)

        return f"Produto {product.name} registrado com sucesso"
    
    def update_amount(self, barcode, new_amount): #poderia receber um objeto produto para padronizar
        stock = self.load_stock()
        for product in stock:
            if product.barcode == barcode:
                product.amount = new_amount
        self.save_stock(stock)
        return "Quantidade do produto atualizada com sucesso"
    
    def delete_product(self, product: Product):#testar se as posições estão funcionando
        stock = self.load_stock()
        position = product.position
        #atualizar o estoque, puxando todos os produtos para uma posição anterior
        #deletar a instancia do produto
        
        for element in range(position, Stock.current_position-1):
            stock[element].position -= 1
            stock[element] = stock[element+1]

        stock.pop(Stock.current_position-1)
        Stock.current_position -= 1

        del product

        self.save_stock(stock)

    def __str__(self):
        pass

        