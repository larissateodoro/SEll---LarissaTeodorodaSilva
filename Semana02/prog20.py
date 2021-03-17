#Uso de blocos e tratamento de erros

try:
   #f = open('testfile.txt')
   f = open('currupt_file.txt')
   #if f.name == 'currupt_file.txt'
      #raise Exception 
   #print(f.read())
   #f.close

except FileNotFoundError as e:
    print(e)

except Exception as e:
    #print(e)
    print('Error!')

else:
    print(f.read())
    f.close()

finally:
    print("Executing Finally...")