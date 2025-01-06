from packages.product import Product
import pickle
import os

class Stock:
    def __init__(self):
        self.file_name = 'stock.pkl'

    def __load_stock(self) -> list[Product]:
        if os.path.exists(self.file_name):
            with open(self.file_name, 'rb') as file:
                return pickle.load(file)
        return []
    
    def __save_stock(self, stock) -> None:
        with open(self.file_name, 'wb') as file:
            pickle.dump(stock, file)

    def register_product(self, product: Product) -> str:
        if not isinstance(product, Product):
            raise ValueError("Formato inválido")

        stock = self.__load_stock()
        stock.append(product)
        self.__save_stock(stock)

        return f"Produto {product.name} registrado com sucesso"
    
    def get_product(self, barcode: int) -> Product:
        stock = self.__load_stock()
        for product in stock:
            if product.barcode == barcode:
                return product
        raise ValueError("Produto não encontrado")    
    
    def update_amount(self, barcode: int, new_amount: int) -> str:
        stock = self.__load_stock()
        for product in stock:
            if product.barcode == barcode:
                product.amount = new_amount
            self.__save_stock(stock)
            return "Quantidade do produto atualizada com sucesso"
        raise ValueError("Produto não encontrado")

    def delete_product(self, barcode: int) -> str:
        stock = self.__load_stock()
        for index, product in enumerate(stock):
            if product.barcode == barcode:
                del stock[index]
                self.__save_stock(stock)
                return "Produto deletado com sucesso"
        raise ValueError("Produto não encontrado")
    
    def list_stock(self) -> None: 
        stock_list = self.__load_stock()
        for product in stock_list:
            print(product)
        return