import turtle

turtle.color('blue') #color de la flecha

#turtle.forward(100) #vector de avance
#
#turtle.left(45) #el argumento se pasa en grados cardinales
#turtle.forward(100)

for i in range(100):
    turtle.forward(50)
    turtle.left(60)

turtle.done()


#*****************************************************

#Actividad

#CUADRADO
def cuadrado(arista=100, color="red"):
    turtle.pen(fillcolor=color)
    turtle.pencolor(color)
    for i in range(4):
        turtle.forward(arista) 
        turtle.left(90)

cuadrado()

def fill_cuadr(arista=100, color="red"):
    turtle.begin_fill()
    cuadrado(arista,color)
    turtle.end_fill()

fill_cuadr(200, "red")

#CIRCULO
def circulo(radio=100,color="blue"):
    turtle.pen(fillcolor=color)
    turtle.pencolor(color)
    turtle.circle(radio)
circulo(100)

def fill_circ(radio=100, color="red"):
    turtle.begin_fill()
    circulo(radio,color)
    turtle.end_fill()

fill_circ(200, "red")



#TRIANGULO
def triangulo(arista=100, color="green"):
    turtle.pen(fillcolor=color)
    turtle.pencolor(color)

    for i in range(3):
        turtle.forward(arista) 
        turtle.left(120)
triangulo(100)

def fill_triang(arista=100, color="green"):
    turtle.begin_fill()
    triangulo(arista,color)
    turtle.end_fill()

fill_triang(200, "red")

#Punto de radio
def turtle_dot(radio=None):
    turtle.home()
    turtle.dot(radio, 'blue')

turtle_dot(100)

#RECTANGULO

def rectangulo(largo=100, alto=50, color="green"):
    turtle.pen(fillcolor=color)
    turtle.pencolor(color)    
    for i in range(2):
        turtle.forward(largo)
        turtle.left(90)
        turtle.forward(alto)
        turtle.left(90)

rectangulo(200,50)

def fill_rect(largo=100, alto=50, color="green"):
    turtle.begin_fill()
    rectangulo(largo,alto,color)
    turtle.end_fill()

fill_rect(200,100)

#HEXAGONO
def hexagono(arista=100,color="blue"):
    turtle.pen(fillcolor=color)
    turtle.pencolor(color)
    turtle.circle(arista, extent=None, steps=6)

def fill_hex(arista=100,color="blue"):
    turtle.begin_fill()
    hexagono(arista,color)
    turtle.end_fill()

fill_hex(200, "red")


#ESTRELLA
def estrella_9():
    turtle.pen(fillcolor="red")
    turtle.pencolor('red')
    for i in range (9):
        turtle.forward(100)
        turtle.right(160)

def fill_funct(funcion):
    turtle.begin_fill()
    funcion()
    turtle.end_fill()

fill_funct(estrella_9)

#ESTRELLA
def estrella_5():
    turtle.pen(fillcolor="red")
    turtle.pencolor('red')
    for i in range (5):
        turtle.forward(100)
        turtle.right(144)

def fill_funct(funcion):
    turtle.begin_fill()
    funcion()
    turtle.end_fill()

fill_funct(estrella_5)
