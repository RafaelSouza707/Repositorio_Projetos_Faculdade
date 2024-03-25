# Import de modulos criados no arquivo listaprodutos.
from modulo.listaprodutos import lista_frutas, lista_verduras # -> Importe dos produtos existentes.
from server.caixaQuitanda import *
import os
import time
import sys


# Funcao para realizar a mostragem dos produtos baseado na escolha do cliente na na funcao menu.
def escolha(name, answer):
    # Chamada para listagem das frutas.
    print('{:>25}   {:>14}  {:>14}'.format('ID', 'PRODUTO', 'VALOR'))
    if answer == 1:
        for i in range(0, len(lista_frutas)):
            if i < 9:
                tabela(lista_frutas[i]['id'], lista_frutas[i]['produto'], lista_frutas[i]['valor'])
            else:
                tabelaDeci(lista_frutas[i]['id'], lista_frutas[i]['produto'], lista_frutas[i]['valor'])
        print()
        menuCompra(name, lista_frutas, answer)
    # Chamada para listagem das verduras.
    if answer == 2:
        for i in range(0, len(lista_verduras)):
            if i < 9:
                tabela(lista_verduras[i]['id'], lista_verduras[i]['produto'], lista_verduras[i]['valor'])
            else:
                tabelaDeci(lista_verduras[i]['id'], lista_verduras[i]['produto'], lista_verduras[i]['valor'])
        print()
        menuCompra(name, lista_verduras, answer)

valorTotal = float()

# Funcaos para criar tabela dos produtos que estao a venda.
# Funcao 'tabela' cria para id's com valores com uma casa decimal, e a funcao 'tabelaDeci' cria para valores com duas casas decimais
def tabela(id, produto, valor):
    print("{:>25}   {:>14}  {:>14}".format(id, produto, valor))
def tabelaDeci(id, produto, valor):
    print('{:>26}   {:>13}  {:>14}'.format(id, produto, valor))

# Funcao carrinho de compras onde exibe os itens que estao sendo comprados pelo cliente.
def carrinho(vetorlistaprodutos):
    listaFruta = vetorlistaprodutos[0]
    listaVerdura = vetorlistaprodutos[1]
    print()
    print("Carrinho de compras:")
    print(100*'=')
    print("{:>27} {:>14} {:>10}".format("Produto:", "Quantidade:", " Valor (R$):"))
    global valorTotal
    valorTotal = float()
    for produto in range(0, len(listaFruta)):
        idproduto = listaFruta[produto][0]
        ids = lista_frutas[int(idproduto-1)]['produto']
        qtds = listaFruta[produto][1]
        valor = lista_frutas[int(idproduto-1)]['valor']
        valorTotalFruta = valor*qtds
        valorTotal += valorTotalFruta
        print("{:>26} {:>12} {:>12.2f}".format(ids, qtds, valorTotalFruta))
    for produto in range(0, len(listaVerdura)):
        idproduto = listaVerdura[produto][0]
        ids = lista_verduras[int(idproduto-1)]['produto']
        qtds = listaVerdura[produto][1]
        valor = lista_verduras[int(idproduto-1)]['valor']
        valorTotalVerdura = valor*qtds
        valorTotal += valorTotalVerdura
        print("{:>26} {:>12} {:>12.2f}".format(ids, qtds, valorTotalVerdura))
    print(100*"-")
    print("{:>18}Valor Total da Compra: {:>11.2f}".format("", valorTotal))

# Tabela do produtos que estao sendo comprados.
def carrinhoPagamento(vetorlistaprodutos):
    listaFruta = vetorlistaprodutos[0]
    listaVerdura = vetorlistaprodutos[1]
    print(100*'=')
    print("{:>27} {:>14} {:>10}".format("Produto:", "Quantidade:", " Valor (R$):"))
    global valorTotal
    valorTotal = float()
    for produto in range(0, len(listaFruta)):
        idproduto = listaFruta[produto][0]
        ids = lista_frutas[int(idproduto-1)]['produto']
        qtds = listaFruta[produto][1]
        valor = lista_frutas[int(idproduto-1)]['valor']
        valorTotalFruta = valor*qtds
        valorTotal += valorTotalFruta
        print("{:>26} {:>12} {:>12.2f}".format(ids, qtds, valorTotalFruta))
    for produto in range(0, len(listaVerdura)):
        idproduto = listaVerdura[produto][0]
        ids = lista_verduras[int(idproduto-1)]['produto']
        qtds = listaVerdura[produto][1]
        valor = lista_verduras[int(idproduto-1)]['valor']
        valorTotalVerdura = valor*qtds
        valorTotal += valorTotalVerdura
        print("{:>26} {:>12} {:>12.2f}".format(ids, qtds, valorTotalVerdura))
    print(100*"-")
    print("{:>18}Valor Total da Compra: {:>11.2f}".format("", valorTotal))


# Lista para anexacao dos itens associados ao cliente. # A posicao 0 é referente a lista de produtos da listagem de frutas adicionados pelos clientes, e a posicao 1 para verduras.
listaProdutos = [[],[]]


# Funcao menu para compra o parametro é o vetor das frutas ou verduras.
def menuCompra(name, vetorProdutos, answer):
    continueAte = False
    while continueAte == False:
        compraProduto = input("""
                                MENU DE COMPRA:
                                ADICIONE O ID DO PRODUTO QUE DESEJA COMPRAR E SE QUISER COLOQUE A QUANTIDADE. (usando um espaço entre o ID e a QUANTIDADE):
                                
                                [111] - PARA CANCELAR A COMPRA E VOLTAR PARA O MENU PRINCIPAL
                                [122] - PARA VERIFICAR O CARRINHO DE COMPRA
                                [133] - PARA MUDAR A OPCAO DE COMPRA
                                [144] - PARA FINALIZAR A COMPRA
                                
                                """).split()

        if not compraProduto or not compraProduto[0].isdigit():
            print("Entrada inválida!")
            continue
        id_produto = int(compraProduto[0])
        if id_produto == 111:
            global listaProdutos
            continueAte = True
            menu(name, testeFalse = False)
        elif id_produto == 122:
            carrinho(listaProdutos)
            menu(name, testeFalse = False)
        elif id_produto == 133:
            menu(name, testeFalse = False)
        elif id_produto == 144:
            finalizarCompra(name, listaProdutos)
            continueAte = True
        # Dentro desta condicional alem de adicionar o item na cesta/carrinho de compras, ela verifica a existenia do produto no carrinho. Caso exista há o incremento da quantidade que está sendo comrpado o item.
        elif 1 <= id_produto <= 19:
            print()
            print(100*'=')
            quantidade = int(compraProduto[1]) if len(compraProduto) > 1 and compraProduto[1].isdigit() else 1
            print('O SEGUINTE PRODUTO FOI ADICIONADO AO CARRINHO DE COMPRAS:')
            if vetorProdutos == lista_frutas:
                v = int(compraProduto[0])
                print(lista_frutas[v-1]['produto'])
                atualizado = False
                for i, (id_prod, qtd) in enumerate(listaProdutos[0]):
                    if id_prod == id_produto:
                        listaProdutos[0][i] = (id_prod, qtd + quantidade)
                        atualizado = True
                        break
                if not atualizado:
                    listaProdutos[0].append((id_produto, quantidade))
            elif vetorProdutos == lista_verduras:
                v = int(compraProduto[0])
                print(lista_verduras[v-1]['produto'])
                atualizado = False
                for i, (id_prod, qtd) in enumerate(listaProdutos[1]):
                    if id_prod == id_produto:
                        listaProdutos[1][i] = (id_prod, qtd + quantidade)
                        atualizado = True
                        break
                if not atualizado:
                    listaProdutos[1].append((id_produto, quantidade))
            print(100*'=')
            escolha(name, answer)
        else:
            print('ID de produto inválido!')

def print3L():
    print()
    print()
    print()

# Funcao para finalizar a compra.
def finalizarCompra(name, listaCarrinho):
    print('CONFIRMAR A COMPRA:')
    global listaProdutos
    global valorTotal
    global caixaTotal
    answer = int(input("""
                        [1] - PARA FINALIZAR A COMPRA
                        [2] - PARA VOLTAR AO MENU PRINCIPAL
                        [3] - PARA CANCELAR A COMPRA
          """))
    if answer == 3:
            listaProdutos = [[],[]]
            valorTotal = float()
            menu(name, testeFalse = False)
    elif answer == 1:
        print3L()
        print('CONFIRMANDO PAGAMENTO.')
        novaCaixa = caixaTotal + ({'idvalor':valorTotal},)
        with open('server/caixaQuitanda.py', 'w') as file:
            file.write(f"caixaTotal = {novaCaixa}\n")
        for _ in range(80): # -> Animacao do processamento da compra.
            sys.stdout.write('\rCarregando |')
            sys.stdout.write('─' * _)
            sys.stdout.write(' ' * (79 - _) + '|')
            sys.stdout.flush()
            time.sleep(0.02)
        print3L()
        print("""
                                    RECIBO ELETRONICO:
                                   
                  Cliente: {} 
                  
                  PRODUTOS COMPRADOS:
                  """.format(name))
        carrinhoPagamento(listaCarrinho)
        print("""
                OBRIGADO E VOLTE SEMPRE!
              """)
        soma_total_valores = sum(item["idvalor"] for item in novaCaixa)
        print("O valor total de vendas da Quintande é de: ", soma_total_valores)
        return sys.exit()
    elif answer == 2:
        menu(name, testeFalse = False)


# Funcao do menu do app que está atrelada ao client logado no server.
def menu(name, testeFalse):
    global listaProdutos
    global valorTotal
    while testeFalse == False:
        answer = int(input("""
                                SEJA BEM VINDO AO QUITANDA:
                                MENU:
                                    [1] - COMPRAR FRUTAS
                                    [2] - COMPRAR VERDURAS
                                    [3] - CARRINHO DE COMPRAS
                                    [4] - CANCELAR
                                    [5] - FINALIZAR COMPRA
                            """))
        if answer == 4:
            valorTotal = float()
            testeFalse = True
            return sys.exit()
        else:
            if answer == 1:
                print("""
                        BEM VINDO A SEÇÃO DE FRUTAS
                      """)
                print(100*'=')
                print()
                escolha(name, answer)
            elif answer == 2:
                print("""
                        BEM VINDO A SEÇÃO DE VERDURAS
                      """)
                print(100*'=')
                print()
                escolha(name, answer)
            elif answer == 3:
                carrinho(listaProdutos)
            elif answer == 5:
                finalizarCompra(name, listaProdutos)
            else:
                menu(name, answer)