import socket
import threading
import os


HOST = 'localhost'
PORT = 50000
ADDR = (HOST, PORT)
FORMATO = 'utf-8'


# servidor recebe parametro socket.socket que sao atribuidos os caracteristicas de conexao que serao usados, AF_INET (constante que indica que o endereço de socket pertence ao IPv4) e SOCK_STREAM (protocolo TCP-IP).
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(ADDR) # -> O comando 'bind' recebe um unico parametro.

# Listas globais de user's.
conexoes = []
mensagens = []

# Funcao que cria novo user com os parametros estabelecidos.
def criarUsuario(caminho_completo, name):
    # Transfere os parametros adequeados.
    arq_origem = "servidorPython/client/defaultUser.py"
    arq_destino = caminho_completo
    with open(arq_origem, "r") as origem:
        conteudo = origem.read()
        
        with open(arq_destino, "w") as destino:
            destino.write(conteudo)
        with open(arq_destino, "r") as makeUser:
            linhas = makeUser.readlines()
    linhas_modifica_name = linhas[2].replace('nomeNewUser', name)
    linhas[2] = linhas_modifica_name
    with open(arq_destino, 'w') as arquivo:
        arquivo.writelines(linhas)


# Funcao que verifica se o nome do user existe, caso nao exista ele cria um arquivo dedicado ao user com inforamçoes relacionadas a ele. Ex: carrinho de compras e historico de compras.
def verificaNome(nome, cliente, end):
    nomeSplit = nome.split(" ") # -> Transforma o nome do user em uma tupla com a divisao pelos espaços entre os termos.
    nomeClient = '_'.join(nomeSplit) # -> Tranforma o nome em um str com espaçamento com "_".
    client = f"{nomeClient}.py" # -> Cria o nome do serquivo que será dedicado ao cliente no foramto py.
    caminho = "servidorPython/client/userClient" # -> Variavel com o caminho que será usado na logica do algoritmo para criar/alterar o arquivo dedicado ao cliente.
    caminho_completo = os.path.join(caminho, client) # -> Variavel com todo o caminho para o arquivo do clente.
    
    # Bloco de verificaçao da existencia do user nos arquivos do server. Caso nao exista um novo user é criado no else.
    if os.path.exists(caminho_completo):
        print('Cliente logado: ', client) # -> Mensagem para servidor.
        return True
    else:
        with open(caminho_completo, "x") as arquivo:
            criarUsuario(caminho_completo, nome)
            print('Novo cliente criado: ', end) # -> Mensagem para servidor.
            arquivo.close()
        return True

def clientesAtivos():
    print('Cliente conectados:')
    for conexao in range(0, len(conexoes)):
            teste = conexoes[conexao]['nome']
            print(teste)


# Funcao que chama a criacao dos user na lista de conectados.
def validacaoCliente(cliente, end):
        print("[Nova conexao]: ", end) # -> Mensagem para servidor.
        nome = cliente.recv(1024).decode(FORMATO) # -> Recebe o nome do user.
        nomeSplit = nome.split(" ") # -> Pega o nome do user e transforma em lista de str.
        global conexoes # -> Chamada da lista para o escopo da funçao.
        data = cliente.recv(1024).decode(FORMATO) # -> Recebe a resposta do user do primeiro menu que aparece para o user.
        if data == '2':
            # Remover usuário logado ao sair.
            usuario = conexoes.pop(end, None)
            if usuario:
                print(f"Usuário {nomeSplit} saiu.")
                clientesAtivos()
        if data == '1':
        # Cria na lista 'conexoes' a entrada do novo user.
            if verificaNome(nome, cliente, end) == True:
                conn_map = {
                    "conn": cliente,
                    "end" : end,
                    "nome" : nomeSplit,
                }
                conexoes.append(conn_map)
        clientesAtivos()

# Funcao que da inicio a conexao com cliente que por sua vez é atribuido ao sistema uma nova operaçao.
def start():
    # listen() faz o servidor ouvir a mensagem enviada pelo usuario.
    servidor.listen()
    print('Aguardando conexao com cliente...')
    while True:
        cliente, end = servidor.accept() # -> Para a conexao entre cliente e servidor usa-se accept().
        thread = threading.Thread(target=validacaoCliente, args=(cliente, end)) # -> Cria uma nova threading para que o cliente entao possa realizar a operacao da execucao dos scripts.
        thread.start()


start()
servidor.close()