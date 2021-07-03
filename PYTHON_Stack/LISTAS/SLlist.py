
class SLNode:
	def __init__(self, val):
		self.value = val
		self.next = None


class SList:
    def __init__(self):
        self.head = None 

    def add_to_front(self, val):  # agrega la linea, toma un valor
        # crea una instancia de la clase Node usando el valor dado
        new_node = SLNode(val)
        current_head = self.head  # salva la cabecera actual en una variable
        # Coloca el proximo nodo en la lista de la cabecera actual
        new_node.next = current_head
        # Coloca la lista de la cabecera al nodo que se creó en el paso anterior
        self.head = new_node
        return self	                # return self para permitir las cadenas

    def print_values(self):
        runner = self.head  # un puntero al primer nodo de la lista
        while (runner != None):  # iterando mientras el corredor es un nodo y no ninguno
            print(runner.value)  # imprimir el valor del nodo actual
            runner = runner.next 	# Establecer el corredor a su vecino
        return self	   # Una vez que el bucle está terminado, regrese a sí mismo para permitir el encadenamiento

    def add_to_back(self, val):  # acepta un valor
        if self.head == None:  # si la lista está vacia
            self.add_to_front(val)  # ejecuta el método add_to_front
            return self  # asegurémonos de que el resto de esta función no suceda si agregamos al frente
		# crea una nueva instancia de nuestra clase Node con el valor dado
        new_node = SLNode(val)
        runner = self.head 	# establece un iterador para que comience al principio de la lista
        while (runner.next != None):  # iterador hasta que el iterador no tenga un vecino
			# Incrementa el corredor al siguiente nodo de la lista.
            runner = runner.next
		# Incrementa el corredor al siguiente nodo de la lista.
        runner.next = new_node
        return self             # retorna self para permitir el encadenamiento

    def remove_from_front(self):
        runner = self.head
        self.head = runner.next
        return self

    def remove_last(self):
        if(self.head != None and self.head.next != None):
            runner = self.head
            while(runner.next.next != None):
                runner = runner.next
            runner.next = None
        elif(self.head.next == None):
            self.head.value = None
        return self
    
    def remove_val(self, val):
        runner = self.head
        #eliminar primer nodot
        if runner.value == val:
            self.head = runner.next
        while runner.next.value != val:
            runner = runner.next
        temp= runner.next
        runner.next = None
        runner.next = temp.next
        return self

    def insert_at(self, val, n):
        runner = self.head
        if n==0:
            self.add_to_front(val)
        else:
            contador = 1
            while contador< n:
                runner = runner.next
                contador += 1
            temp = runner.next
            nuevo = SLNode(val)
            runner.next = nuevo
            nuevo.next = temp
        return self


my_list = SList()	# crear una nueva instancia de una lista
my_list.add_to_back("1").add_to_back("2").add_to_back("3").add_to_back("4").insert_at("5", 0).print_values()    # encadenamiento, yeah!



my_list = SList()  # crear una nueva instancia de una lista
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # encadenamiento, yeah!
