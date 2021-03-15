

#Básicos:
#f = open("test.txt", "r")
#f = open("test.txt", "w")
#f = open("test.txt", "a")
#f = open("test.txt", "r+")
#print(f.name)
#print(f.mode)
#f.close()

#Outra forma 

with open('test.txt','r') as f:
    pass 
print(f.closed)

print(f.read())

#Outra forma
with open('test.txt','r') as f:
    f_contents = f.read()
    print(f_contents)

# Mostra rodas as linhas do arquivo

 with open('test.txt','r') as f:
    f_contents = f.readlines() 
    print(f_contents)
#

 with open('test.txt','r') as f:
    f_contents = f.readline() #sem o 's' mostra só a primeira linha
    print(f_contents, end = '')

    f_contents = f.readline() 
    print(f_contents, end= '')

#lê todas as linhas
	for line in f:
		print(line, end = '')

#Imprime a lista
	f_contents = f.read()
	print(f_contents, end = '')

	#Imprimi o 100 primeiros caracteres:
	f_contents = f.read(100)
	print(f_contents, end = '')
	#Imprime o resto do arquivo pois imprime mais 100 caracteres
    f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')

	#Trabalhado com pequenas partes
	size_to_read = 100
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size_to_read)

	#Interação com pequenos pedaços com 10 caracteres
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')

	f.seek(0) #retorna no inicio

	f_contents = f.read(size_to_read)
	print(f_contents, end = '')

	print(f.tell())

	while len(f_contents) > 0:
		print(f_contents, end = '*')
		f_contents = f.read(size_to_read)
print(f.mode)
print(f.closed)
print(f.read())


#Apresenta um erro pois está só para leitura
with open("test.txt", "r") as f:
	f.write("Test")

#Escrevendo 
with open("test2.txt", "w") as f:
	pass
	f.write("Test")
	f.seek(0)
	f.write("Test")
	f.seek("R")

#Copiando arquivos
with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)

#Copiando uma imagem
#Forma errada, pois copia como texto
with open("bronx.jpg", "r") as rf:
	with open("bronx_copy.jpg", "w") as wf:
		for line in rf:
			wf.write(line)

#Copiando uma imagem em bytes
with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		for line in rf:
			wf.write(line)

###Copiando partes  das imagens
with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)