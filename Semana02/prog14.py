#Renomeação de arquivos e aautomatização 

import os

#diretório que contem os arquivos
os.chdir('/Users/Larissa/Videos/')
print(os.getcwd())
print(dir(os))

#Imprime todos os nomes de arquivo atuais
for f in os.listdir():
    #print(f)
    #print(os.splitext(f))


    file_name, file_ext = os.path.splitext(f)
    # print(file_name)

    f_title, f_course, f_number = file_name.split('-')

    
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()
#Formato que vai aparecer
    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

f_num = f_num.strip()[1:]

f_num = f_num.strip()[1:].zfill(2) #coloca dois digitos

    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    
    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)
