import concurrent.futures
import time

#Começa a marcar o tempo(inicio do contador)
start = time.perf_counter()

#Função que "dorme" por segundos e depois retorna esse tempo
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#Criação de Multiprocessos
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1] #Lista a ser executada
    results = executor.map(do_something, secs) #Mapeia a função
   
    #Retorna os dados na ordem que foram iniciados
    #for result in results:
        #print(result)
#Para o tempo de processamento
finish = time.perf_counter()

#Imprime o tempo gasto em segundos
print(f'Finished in {round(finish-start, 2)} second(s)')