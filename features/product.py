class Product:
    def __init__(self, barcode, name, price, amount):
        self._barcode = int(barcode)
        self._name = name
        self._price = float(price)
        self._amount = int(amount)
        
    @property
    def get_barcode(self):
        return self._barcode
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_amount(self):
        return self._amount
    
    @property
    def get_price(self):
        return self._price
    
    @property.setter
    def set_barcode(self, new_barcode):
        if type(new_barcode) != int:
            raise ValueError("O código de barras deve ser um número inteiro")
        
        self._barcode = new_barcode
        return self._barcode
    
    @property.setter    
    def set_name(self, new_name):
        if type(new_name) != str:
            raise ValueError("O nome deve ser uma palavra")
        
        self._name = new_name
        return self._name   
    
    @property.setter
    def set_amount(self, new_amount):
        if type(new_amount) != int:
            raise ValueError("A quantidade deve ser um número inteiro")
        
        self._amount = new_amount
        return self._amount
    
    @property.setter
    def set_price(self, new_price):
        if type(new_price) != float and type(new_price) != int:
            raise ValueError("O preço deve ser um número")
        
        self._price = new_price
        return self._price
    
    def __str__(self):
        return f"Barcode: {self._barcode}, Name: {self._name}, Price: {self._price}, Amount: {self._amount}"