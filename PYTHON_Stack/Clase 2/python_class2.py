nombre = "Zen"
print("Mi nombre es", nombre)
print("mi nombre es {}".format(nombre))

hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3 
print(hw, py)

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# actualiza si la llave existe
new_person['hobbies'] = ['climbing', 'coding']	# agrega un par clave-valor si la clave no existe
print(new_person)	
# salida: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# remueve la clave especifica y retorna el valor
print(w)		# salida: 160.2
print(new_person['name'])	