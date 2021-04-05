import socket 

class Servidor:
    def __init__(self, porta, file):
        self._hostServer = '127.0.0.1'
        print('IP: ',self._hostServer)
        self._port = int(porta)  #Parâmetro
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Para criar o socket do tipo tcp
        self._address = (self._hostServer, self._port)# Passa IP e Porta
        self._tcp.bind(self._address)# Passa o endereço para a conexão TCP
        self._tcp.listen(1)# Só pode fazer uma conexão no servidor
        self._nameFile = file # Muda Parâmetro
    
    def closeConnection(self):
        self._tcp.close()
    
    def readFile(self):#Para ler o arquivo
    
            self._fileOpen = open(self._nameFile, "rb")#Abrindo o arquivo
            self._envio = self._fileOpen.read()#Lendo o arquivo
            self._fileOpen.close()#Fecha o fluxo de arquivo
          
    def sendFile(self):#Enviando o arquivo
        print ('Conectado...')
        self._connection, self._client = self._tcp.accept()
        print ('Conectado por', self._client)      
        self._connection.sendall(self._envio)#Enviando o arquivo
    
class Cliente:
    def __init__(self, IP , porta , file ):
        self._hostServer = IP
        self._port = int(porta)            # Parâmetro
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Criando conexão com servidor
        self._address = (self._hostServer, self._port)#Passa o IP e a Porta
        print ('Esperando cliente...')
        self._tcp.connect(self._address) #Conectando com o Cliente
        print ('Conectado!')
        self._nameFile = file #Parâmetro
    #Fecha conexão TCP
    def closeConnection(self):
        self._tcp.close()
    
    #Recebe arquivo
    def receiveFile(self):
        with open(self._nameFile,'wb') as wf:
            while True:
                self._recebido = self._tcp.recv(4096)
                if not self._recebido: break #Se não tiver valor no recebido
                wf.write(self._recebido)