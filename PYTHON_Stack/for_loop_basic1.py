#Básico : imprime todos los enteros del 0 al 150.
i=0
while i<=150:
    print(i)
    i+=1

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range(1,201):
    print(x*5)

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for x in range(1,101):
    if (x%10==0):
        print("Coding Dojo")
        continue
    elif (x%5==0):
        print("Coding")
        continue
    print(x)

#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
sum_odd=0
x=0
while x < 500000:
    if x%2!=0:
        sum_odd+=x
        x+=1
        continue
    x+=1
print(sum_odd)

#Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for x in range (2018,0,-4):
    print(x)

#Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum=2
highNum=10
mult=2
for x in range(lowNum,highNum+1):
    if x%mult==0:
        print(x)

#BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?
Primos=[]
x=1
target=1000
while x<=target+1:
    mult=0
    for y in range(2,target+1):
        if x%y==0:
            mult+=1
    if mult==1:
        Primos.append(x)
    x+=1
print(Primos)