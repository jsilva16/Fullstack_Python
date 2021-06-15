# Actualiza los valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1. Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].

x[1][0]=15

#2. Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'

students[0]['last_name']='Bryant'

#3. En el directorio sports_directory, cambia 'Messi' a 'Andres'

sports_directory['soccer'][0]='Andres'

#4. Camba el valor 20 en z a 30

z[0]['y']=30

#////////////////////////////////////////////////////////////////////////////////////////////////////

#Itera a través de una lista de diccionarios

#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista 
# e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(arr):
    for i in range (len(arr)):
        print([key for key in arr[i].keys()][0]+" - "+[value for value in arr[i].values()][0] + ", "
        +[key for key in arr[i].keys()][1]+" - "+[value for value in arr[i].values()][1])
        


iterateDictionary(students)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios
#  y un nombre de clave, la función imprima el valor almacenado en esa clave para cada 
# diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key, arr):
    for i in range (len(arr)):
        print([value for value in arr[i].values()][0] + ", "
        +[key for key in arr[i].keys()][1]+" - "+[value for value in arr[i].values()][1])