class Product:
    def __init__(self, barcode, name, price, amount):
        self._barcode = int(barcode)
        self._name = name
        self._price = float(price)
        self._amount = int(amount)
        
    @property
    def barcode(self):
        return self._barcode
    
    @barcode.setter
    def barcode(self, new_barcode):
        if type(new_barcode) != int:
            raise ValueError("O código de barras deve ser um número inteiro")
        
        self._barcode = new_barcode
    
    @property
    def name(self):
        return self._name
    
    @name.setter    
    def name(self, new_name):
        if type(new_name) != str:
            raise ValueError("O nome deve ser uma palavra")
        
        self._name = new_name

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, new_amount):
        if type(new_amount) != int:
            raise ValueError("A quantidade deve ser um número inteiro")
        
        self._amount = new_amount

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if type(new_price) != float and type(new_price) != int:
            raise ValueError("O preço deve ser um número")
        
        self._price = new_price
    
    def __str__(self):
        return f"| Nome: {self._name} | Código: {self._barcode} | Preço: {self._price:.2f} | Quantidade: {self._amount} |"
    