from managementSys import ManagementSystem
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

app = ManagementSystem()

while True:

    clear()
    print("\nBem vindo ao sistema de vendas")
    print("O que deseja fazer?")
    choice = input("[1] Cadastro de produtos\n[2] Listagem do estoque\n[3] Atualizar quantidade no estoque\n[4] Remover produto do estoque\n[5] Página de vendas\n[s] Sair\n")

    if choice == 's':
        break

    while choice == '1':
        clear()
        print("\nCadastro de produtos")
        barcode = int(input("Digite o código de barras: "))

        try:
            app.get_product(barcode)
            print("Produto já cadastrado.\n")
            time.sleep(2)
            continue
        except ValueError:
            pass

        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        amount = int(input("Digite a quantidade do produto: "))
        
        try:
            print(app.register_product(barcode, name, price, amount),"\n")
        except ValueError as error:
            print(error,"\n")
            continue

        answer = input("Deseja cadastrar mais produtos? [s/n]\n")
        if answer == 's':
            continue
        elif answer == 'n':
            choice = None

    if choice == '2':
        clear()
        print("\nListagem do estoque")
        app.list_stock()
        print("\n")

        if input("Pressione Enter para voltar ao menu.") != None:
            choice = None

    if choice == '3':
        clear()
        barcode = int(input("\nDigite o código de barras do produto que deseja atualizar a quantidade:\n"))
        new_amount = int(input("Digite a nova quantidade:\n"))
        
        try:
            print("\n",app.update_amount(barcode, new_amount))
            print(app.get_product(barcode),"\n")
        except ValueError as error:
            print(error, "\n")
            continue

    if choice == '4':
        clear()
        barcode = int(input("\nDigite o código de barras do produto que deseja remover:\n"))
        
        try:
            print(app.delete_product(barcode))
            time.sleep(2)
        except ValueError as error:
            print(error, "\n")
            time.sleep(2)
            continue

    while choice == '5':
        clear()
        print("\nPágina de vendas")
        sale = app.new_sale()
        
        while True:
            clear()
            print("\nVenda em andamento:")
            print("Para finalizar a venda, digite '-1' quando for solicitado o código de barras do produto.\n\n")
            
            sale.list_sale()
            barcode = int(input("\n\nCódigo de barras: "))
            
            if barcode == -1:
                break
            
            try:
                sale.add_product(barcode, 1)
            except ValueError as error:
                print(error)
                time.sleep(2)
                continue
            
        remove = input("\nDeseja remover algum produto da venda? [s/n]\n")
        if remove == 's':
            while True:
                clear()
                print("\nVenda em andamento:")
                sale.list_sale()
                barcode = int(input("\n\nCódigo de barras do produto que deseja remover: "))
                
                try:
                    print(sale.remove_product(barcode))
                except ValueError as error:
                    print(error)


                remove_more = input("\nDeseja remover mais produtos? [s/n]\n")
                if remove_more == 's':
                    continue
                elif remove_more == 'n':
                    break

        clear()
        print("\n\nResumo da venda:")
        sale.list_sale()
        
        print("\nObrigado pela compra!\n")

        if input("Pressione Enter para voltar ao menu.") != None:
            choice = None