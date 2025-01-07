from packages.stock import Stock

class Sales:
    def __init__(self, stock):
        self._stock = stock
        self.total_payable = 0.0
        self.sale_items = []

    def add_product(self, barcode: int, sale_amount = 1) -> str:
        try:
            product = self._stock.get_product(barcode)
        except ValueError as error:
            raise error
      
        if product.amount < sale_amount:
            raise ValueError("Quantidade insuficiente")
        
        product.amount -= sale_amount
        self._stock.update_amount(barcode, product.amount)

        for item in self.sale_items:
            if item['barcode'] == barcode:
                item['amount'] += sale_amount
                return "Produto adicionado com sucesso"
            
        self.sale_items.append({
            'barcode': barcode,
            'name': product.name,
            'price': product.price,
            'amount': sale_amount
        })
        return "Produto adicionado com sucesso!"
    
    def remove_product(self, barcode: int) -> str:
        for item in self.sale_items:
            if item['barcode'] == barcode:
                self.sale_items.remove(item)
                product = self._stock.get_product(barcode)
                product.amount += item['amount']
                self._stock.update_amount(barcode, product.amount)
                return "Produto removido com sucesso!"
        raise ValueError("Produto não encontrado.")
    
    def __close_sale(self) -> float:
        self.total_payable = 0.0
        for product in self.sale_items:
            self.total_payable += product['price'] * product['amount']
        return self.total_payable
    
    def list_sale(self):
        for product in self.sale_items:
            barcode = product['barcode']
            name = product['name']
            price = product['price']
            amount = product['amount']
            print( f"({barcode}) {name}  {amount} X R$ {price:.2f}")
        print(f"--> Total: R$ {self.__close_sale():.2f}")

    #método para relatório de venda
    #método para remover unidades de um produto que está na venda