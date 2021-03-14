
def hello_func():
    print('Hello Function.')

hello_func()
hello_func()
hello_func()
hello_func()

def hello_func1():
    return 'Helo Function'

print(hello_func1())  

print(len('Test'))
print(hello_func1().upper()) 

#Argumentos
def hello_func1(greeting, name='You'):
     return '{}' .format(greeting, name)

print(hello_func1('Hi')) 

def hello_func1(greeting, name='You'):
     return '{}, {}'.format(greeting, name)

print(hello_func1('Hi', name = 'Corey')) 

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
#Trabalhando com listas
courses= ['Math', 'Art']
info = {'name':'John', 'age': 22}

student_info(*courses, **info)
student_info ('Math','Art', name = 'John', age = 22)

#Codigo do final do video
#Dias de cada mes
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

#Condições para os anos bissextos
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    """Retorna número de dias e meses do ano"""
    """Primeiro verifica se o mês está entre 1 e 12"""
    if not 1 <= month <= 12:
      return 'Invalid Month'
    if month == 2 and is_leap(year):
     return 29
    return month_days[month]

print (is_leap(2020))
print(days_in_month(2017,2))