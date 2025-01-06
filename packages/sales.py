from packages.stock import Stock

class Sales:
    def __init__(self, stock: Stock):
        self._stock = stock
        self.total_payable = 0.0
        self.sale = []

    def add_product(self, barcode: int, sale_amount = 1) -> str:
        product = self._stock.get_product(barcode)
        if product.amount < sale_amount:
            raise ValueError("Quantidade insuficiente")
        
        product.amount -= sale_amount
        self._stock.update_amount(barcode, product.amount)
        self.sale.append(product)
        self.total_payable += product.price * sale_amount
        return "Produto adcionado com sucesso"
    
    def remove_product(self, barcode: int, sale_amount = 1) -> str:
        product = self._stock.get_product(barcode)
        if product in self.sale:
            self.sale.remove(product)
            product.amount += sale_amount
            self._stock.update_amount(barcode, product.amount)
            self.total_payable -= product.price * sale_amount
            return "Produto removido com sucesso"
        return "Produto não encontrado"
    
    def list_sale(self) -> list[str]:
        return [str(product) for product in self.sale]