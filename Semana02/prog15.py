#Como ler, analisar e gravar arquivos
 #CSV torna a analise mais facil
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.Dictreader(csv_file)
    #print(csv_reader)
    #next (csv_reader)
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.Dictwriter(new_file, fieldnames=fieldnames, delimiter='\t') # '-' delimitador, '\t' espaço

        csv_writer.writeheader()

        for line in csv_reader:
            #print(line[2])
            del line['email']
            csv_writer.writerow(line) #Transfere para o novo arquivo as linhas do original
