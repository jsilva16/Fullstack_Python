# Ejercicio Propuesto

# Se necesita realizar una compra de productos en un local comercial
# Se debe imprimir un menu (definir el menu en una función)
# El menú de opciones tienes lo siguiente

    # Menú
    
    # 1. Ingrese el nombre y rut
    # 2. De la lista de productos elija el elemento a comprar
    # 3. Ingrese la cantidad de unidades a comprar
    # 4. Imprimir en pantalla los datos de la compra
        # Nombre: Juanito Perez
        # Rut: 12345678-5
        # Producto comprado: Bebida de 2Lt. # Definir la lista de productos
        # Número de unidades: 3 
        # Precio por unidad: 1500 # Definir la lista de precio
        # Precio total a pagar sin IVA: 4500
        # Precio total a pagar con IVA: ???

productos={
"Coca_cola 2L": 1400,
"Papas fritas": 1000,
"Ramitas":1000,
"Ramitas de queso":1200,
"Monter Energy":1500
}

productos= [{'Nombre':'Coca_cola','Precio':1200,'Stock':15, "cantidad": ""},
            {'Nombre':'Papas fritas','Precio':1000,'Stock':15, "cantidad": ""},
            {'Nombre':'Ramitas','Precio':1200,'Stock':15, "cantidad": ""},
            {'Nombre':'Ramitas de queso','Precio':1200,'Stock':15, "cantidad": ""},
            {'Nombre':'Monter Energy','Precio':1200,'Stock':15, "cantidad": ""}]

carrito=[]

def menu():
    print("***Menú***\n1. Ingrese el nombre y rut\n2. De la lista de productos elija el elemento a comprar\n3. Ingrese la cantidad de unidades a comprar\n4. Imprimir en pantalla los datos de la compra")
    choice=int(input("Ingrese opción de menú: "))
    #while choice>4 and choice<1:
    #    choice=int(input("Ingrese opción de menú: "))
    if choice == 1:
        ingresa_datos()
    return choice

menu()

def ingresa_datos():
    usuario={"nombre":"" , "rut":""}
    usuario["nombre"]=input("Ingrese su nombre: ")
    usuario["rut"]=input("Ingrese su RUT: ")
    print (usuario)

def listaProductos():
    for i in range(len(productos)):
        print(f"{i+1}.", productos[i]["Nombre"], "$",productos[i]["Precio"])
    print("0. Volver al menú")
    choice_prod=6
    while choice_prod!=0:
        choice_prod=int(input("Seleccione el producto: "))
        if choice_prod==0:
            menu()
        carrito.append(productos[choice_prod-1])
        carrito[len(carrito)-1]["cantidad"]=int(input("Seleccione la cantidad: "))

    return carrito




listaProductos()

