
"""Todos atributos  do modulo so
import os
print(dir(os))"""

"""#Mostra a pasta que está
import os
print(os.getcwd())

#Uma pasta especifica
import os
os.chdir('\SD')
print(os.getcwd())

#Todas as pasta que tem no diretorio
import os
os.chdir('\SD')
print(os.listdir())"""

"""#Para renomear um arquivo
import os
os.chdir('\SD')
os.rename('test.txt', 'demo.txt')

#Daoos de um arquivo
from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestaamp(mod_time))

print(os.stat('demo.txt').st_size)"""

#Imprimir t diretórios
import os
from datetime import datetime
os.chdir('\SD')
for dirpath, dirnames, filenames in os.walk('\SD'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#Localização
import os
from datetime import datetime
os.chdir('\SD')

#Adicionanco qrquivo
print(os.environ.get('HOME'))
file_path =os.path.join(os.environ.get('HOME'), + 'test.txt')
print(file_path)

with open(file_path, 'w') as f:
    f.write

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/fgdfgdft'))
print(os.path.isfile('/tmp/fgdfgdft'))
#Divide a raiz do arquivo ou a extensão
print(os.path.splitext('/tmp/text.tx'))

#Deseja ver tudo que está disponivel
print(dir(os.path))
