#Listas

courses = ['History', 'Math', 'Physics','CompSci']
print (courses)

#Comprimento da Lista
print (len(courses))

#Posição
print (courses[0])
print (courses[-1])
print (courses[0:2])
#Da posição 2 até o fim 
print (courses[2:])

#Adicionar item no final 
courses.append('Art')
print (courses)

#Inserir no inicio
courses = ['History', 'Math', 'Physics','CompSci']
courses.insert(0, 'Art')
print(courses)

#Inserir varios itens
courses = ['History', 'Math', 'Physics','CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)
print (courses[0])

courses = ['History', 'Math', 'Physics','CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

#Remove itens da lista
courses = ['History', 'Math', 'Physics','CompSci']
courses.remove('Math')
print(courses)

#Remove ultimo item da lista e mostra que item foi esse
courses = ['History', 'Math', 'Physics','CompSci']
popped=courses.pop()
print(popped)
print(courses)

#Classificação a lista
courses = ['History', 'Math', 'Physics','CompSci']
courses.reverse()
print(courses)

nums = [1,5,2,4,3]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

courses = ['History', 'Math', 'Physics','CompSci']
nums = [1,5,2,4,3]
sorted(courses)
print(courses)

sorted_courses = sorted(courses)
print(sorted_courses)

#Valor maximo e minimo da lista
print(max(nums))
print(min(nums))
#Soma 
print(sum(nums))

#Indice de um item da lista
print(courses.index('CompSci'))
#Verificar se um item está na lista
print('Art' in courses)

#Percorre os itens da lista
for item in  courses:
    print(item)
#Indices
for index, course in enumerate (courses, start=1):
    print(index,course)

#Transformar lista em String
course_str = ','.join(courses)
new_list = course_str.split(',')
print(course_str)
print(new_list)


list_1 = ['History', 'Math', 'Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

#Tupla
#Imutavel
tuple_1 = ['History', 'Math', 'Physics','CompSci']
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

#Sets
cs_courses = {'History', 'Math', 'Physics','CompSci'}
art_courses = {'History', 'Math', 'Art','Design'}
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#Listas vazias, tuplas e sets

#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_sets = set()

