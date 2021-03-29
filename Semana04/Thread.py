import concurrent.futures
#import threading
import time

#Tempo de inicio da execução
start = time.perf_counter()

#Função que "dorme" por segundos e depois retorna esse tempo
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...{seconds}'

threads = []

#Funciona por 10s e dorme por 1,5s/Forma manual
"""for _ in range(10):
   t = threading.Thread(target=do_something, args=[1.5])
   t.start()
   threads.append(t)

for thread in threads:
    thread.join()"""

#O resultado irá esperar até que a função seja concluida
"""with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something,1)
    print(f1.result())"""

#Passa um intervalo de tempo 
#Retorna os resultados e a ordem que foram iniciados
#Criação de Multithreads
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs) #Mapeia a Função

#for results in results:
    #print (results)

  
#t1 = threading.Thread(target=do_something)
#t2 = threading.Thread(target=do_something)

#t1.start()
#t2.start()

#t1.join()
#t2.join()

#Tempo de término
finish = time.perf_counter()

#Imprime o tempo gasto
print(f'Finished in {round(finish-start, 2)} second(s)')