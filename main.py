import tkinter as tk 
from packages.product import Product
from packages.stock import Stock
from packages.sales import Sales

# Products()
# root = Tk()
# root.title('Sistema de gestão de estoque')
# root.geometry('900x600')
# root.minsize(900, 600)
# root.maxsize(900, 600)

#Precisa ter:
#O programa irá se iniciar na página de gestão, com opção de mudar para página de cadastro, de vendas e de estoque
#Main:
#Junta as outras classes em um programa funcional, usando tkinter para a interface visual
#
#As seguintes classes:
#Produtos-
#   É a classe que estrutura todo o programa, as outros irão trabalhar com objetos dessa classe
#   --> código, nome, descricção, preço, quantidade (custo, validade, data de compra)
#Estoque-
#   Mostra uma lista do estoque
#   --> CRUD
#Cadastro-
#   É onde cadastramos novos produtos
#   -->
#Vendas-
#   Deve buscar os produtos pelo código e ir somando os preços
#   --> (forma de pagamento)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exemplo de Páginas no Tkinter")
        self.geometry("400x300")
        
        # Dicionário para armazenar as páginas
        self.pages = {}
        
        # Adiciona as páginas
        for Page in (PaginaInicial, Pagina1, Pagina2):
            page_name = Page.__name__
            frame = Page(parent=self, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_page("PaginaInicial")
    
    def show_page(self, page_name):
        """Exibe a página solicitada"""
        frame = self.pages[page_name]
        frame.tkraise()

class PaginaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Página Inicial", font=("Arial", 16))
        label.pack(pady=20)
        
        btn_pagina1 = tk.Button(self, text="Ir para Página 1",
                                command=lambda: controller.show_page("Pagina1"))
        btn_pagina1.pack(pady=10)
        
        btn_pagina2 = tk.Button(self, text="Ir para Página 2",
                                command=lambda: controller.show_page("Pagina2"))
        btn_pagina2.pack(pady=10)

class Pagina1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Página 1", font=("Arial", 16))
        label.pack(pady=20)
        
        btn_voltar = tk.Button(self, text="Voltar para Página Inicial",
                               command=lambda: controller.show_page("PaginaInicial"))
        btn_voltar.pack(pady=10)

class Pagina2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Página 2", font=("Arial", 16))
        label.pack(pady=20)
        
        btn_voltar = tk.Button(self, text="Voltar para Página Inicial",
                               command=lambda: controller.show_page("PaginaInicial"))
        btn_voltar.pack(pady=10)

app = App()
app.mainloop()