from Prog02 import Servidor
import sys
import concurrent.futures

porta = sys.argv[1]
arquivo = 'FontedeAlimentação.png'

Server = Servidor(porta,arquivo)
Server.readFile()

i = 1
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(Server.sendFile,f'{i}')
    while not Server._flag:
        pass
    print(Server.mensagem)
    i = i+1
    Server._flag = False 