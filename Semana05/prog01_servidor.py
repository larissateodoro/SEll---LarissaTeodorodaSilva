from Prog01 import Servidor
import sys


porta = sys.argv[1]
arquivo = sys.argv[2]

Server = Servidor(porta,arquivo)
Server.readFile()
Server.sendFile()
Server.closeConnection()