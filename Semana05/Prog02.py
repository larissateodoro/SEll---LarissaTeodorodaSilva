import socket 

class Servidor:
    _flag= False
    mensagem = 'msg'

    def __init__(self, porta, file):

        self._hostServer = '127.0.0.1'
        print('IP: ',self._hostServer)
        self._port = int(porta)  #Parâmetro
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Para criar o socket do tipo tcp
        self._address = (self._hostServer, self._port)# Passa IP e Porta
        self._tcp.bind(self._address)# Passa o endereço para a conexão TCP
        self._tcp.listen(999999)# Conexão no servidor
        self._nameFile = file # Muda Parâmetro
    
    def readFile(self):#Para ler o arquivo
    
            self._fileOpen = open(self._nameFile, "rb")#Abrindo o arquivo
            self._envio = self._fileOpen.read()#Lendo o arquivo
            self._fileOpen.close()#Fecha o fluxo de arquivo
          
    def sendFile(self, contador):# Envio servidor
        self.mensagem = f'cliente {contador} Recebi o Arquivo'
        print ('Esperando cliente...')
        self._connection, self._client = self._tcp.accept()
        self._flag = True
        print ('Cliente {} conectado'.format(self._client[0]))      
        self._connection.sendall(self._envio)#envia variavel envio
        self._connection.close()

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