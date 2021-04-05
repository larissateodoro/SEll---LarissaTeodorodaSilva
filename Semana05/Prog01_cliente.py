from Prog01 import Cliente
import sys

ip = sys.argv[1] #Carrega ip
porta = sys.argv[2] #Carrega porta
arquivo = sys.argv[3] #Carrega arquivo

cliente = Cliente(ip,porta,arquivo)
cliente.receiveFile()
cliente.closeConnection()