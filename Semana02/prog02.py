print ('Hello World')

menssage = 'Bob\'s World'
print (menssage)

print(len(menssage))

print(menssage[2])

print(menssage[0:5])

print(menssage.lower())

print(menssage.upper())

print(menssage.count('o'))

print(menssage.find('World'))

new_menssage = menssage.replace ('World' , 'Universo')

print(new_menssage)

new = menssage + ' , ' + new_menssage
print (new)

new1 = '{}! {}! Welcome!'. format(menssage, new_menssage)
print (new1)

print(dir(menssage))

print(help(str))

print(help(str.lower))