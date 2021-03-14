
student = {'name' : 'John', 'age': 25,'courses': ['Math', 'CompSci']}
#Formas de acessar um dado especifico
print(student['name'])
print(student.get('name'))
print(student.get('phone'))

#Editar informações
student['phone'] = '555-5555'
student['name'] =  'Jane'
print(student.get('phone'))
print(student)

student.update ({'name': 'Jane', 'age':26, 'phone': '555-5555'})
print(student)

#Deletar informações
del student['age']
print(student)

student1 = {'name' : 'John', 'age': 25,'courses': ['Math', 'CompSci']}
age = student1.pop('age')
print(student1)
print(age)

#Quantas chaves temos e quais, valores, itens
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

#Percorrer a lista
for key, value in student.items():
    print(key, value)