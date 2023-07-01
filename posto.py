def menu():
    menu_opcoes = """
    [1] Álcool
    [2] Gasolina
    [3] Sair
    
    """
    return input(menu_opcoes)
    

def abastecer_gasolina(litros):
    GASOLINA_ESTOQUE = 1000
    gasolina_preco = 5.2
    
    if litros <= GASOLINA_ESTOQUE:
        valor = litros * gasolina_preco
        GASOLINA_ESTOQUE -= litros

        print(f'Abastecido com sucesso! Valor a pagar: R${valor}')

    else:
        print('Desculpe, não há gasolina suficiente no estoque.')

def abastecer_alcool(litros):
    ALCOOL_ESTOQUE = 800
    alcool_preco = 4.8

    if litros <= ALCOOL_ESTOQUE:
        valor = litros * alcool_preco
        ALCOOL_ESTOQUE -= litros
        print(f'Abastecido com sucesso! Valor a pagar: R$ {valor}')
    else:
        print('Desculpe, não há álcool suficiente no estoque.')


def main():
    while True:
        opcao = menu()

        if opcao == '1':
            litros = int(input('Informe a quantidade de litros que deseja colocar: '))

            litros = abastecer_alcool(litros)

        elif opcao == '2':
            litros = int(input('Informe a quantidade de litros que deseja colocar: '))

            litros = abastecer_gasolina(litros)

        elif opcao == '3':
            break

        else:
            print('Informe uma opção existente!')


main()
