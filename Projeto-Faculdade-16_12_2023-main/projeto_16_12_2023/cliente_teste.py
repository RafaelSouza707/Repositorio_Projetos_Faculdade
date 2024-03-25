import socket
from modulo.app import menu

HOST = '127.0.0.1'
PORT = 50000
FORMATO = ('utf-8')


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inicia conexao do cliente com servidor. 
cliente.connect((HOST, PORT))



fim = False


while not fim:
    result = False
    while result == False:
        name = None
        name = input("Nome do usuario: ")
        cliente.send(name.encode('utf-8')) # -> Envia o nome do user para o server.
        
        while not fim:
            answer = str(input("""
                            Bem vindo.
                            Menu:
                            [1] - Para abrir o a Quitanda.
                            [2] - Para fechar o programa.
                            """))
            
            if answer == '1':
                print('Bem vindo a Quitanda.')
                cliente.send(answer.encode())
                result = menu(name, testeFalse = False)
            elif answer == '2':
                print('Conexao encerrada pelo cliente. Volte sempre.')
                cliente.send(answer.encode())
                
                cliente.close()
                fim = True