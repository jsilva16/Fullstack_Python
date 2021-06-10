
    #1. Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
    #    Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def big_numb(arr):
    for x in range(len(arr)):
        if arr[x]>0:
            arr[x]='Big'
    return arr
print(big_numb([- 1, 3, 5, -5]))

    #2.Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
    #    Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
    #    Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def count_pos(arr):
    count=0
    for x in arr:
        if x>0:
            count+=1
    print(count)
    arr.pop()
    arr.append(count)
    return arr
print(count_pos([- 1,1,1,1]))
print(count_pos([1,6, -4, -2, -7, -2]))

    #3.Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
    #    Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
    #    Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total(arr):
    suma=0
    for x in arr:
        suma += x    
    return suma
print(sum_total([1,2,3,4]))

    #4.Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
    #    Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def avg(arr):
    sum=0
    for x in arr:
        sum+=x
    return sum/len(arr)
print(avg([1,2,3,4]))

    #5.Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
    #    Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
    #    Ejemplo: longitud ([]) debería devolver 0

def length(arr):
    return len(arr)
print(length([37,2]))

    #6.Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
    #    Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
    #    Ejemplo: mínimo ([]) debería devolver False

def minimo(arr):
    if len(arr)==0:
        return False
    min=arr[0]
    for x in arr:
        if x<min:
            min=x
    return min
print(minimo([37,2,1, -9]))
print(minimo([]))

    #7.Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
    #    Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
    #    Ejemplo: máximo ([]) debería devolver False

def maximo(arr):
    if len(arr)==0:
        return False
    max=arr[0]
    for x in arr:
        if x>max:
            max=x
    return max
print(maximo([37,2,1, -9, 42]))
print(maximo([]))

    #8.Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
    #    Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}

def final(arr):
    sum = 0
    min = arr[0]
    max = arr[0]
    dic = {}
    avg = 0
    for x in arr:
        sum += x
        if x > max:
            max = x
        elif x < min:
            min = x
    avg = sum/len(arr)
    dic["SumaTotal"] = sum
    dic["Promedio"] = avg
    dic["Maximo"] = max
    dic["Minimo"] = min
    dic["Longitud"] = len(arr)
    return dic
print(final([37,2,1, -9]))

    #9.Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
    #    Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def reverse(arr):
    temp=0
    for x in range(int(len(arr)/2)):
        temp=arr[x]
        arr[x]=arr[len(arr)-(x+1)]
        arr[len(arr)-(x+1)]=temp
    return arr
print(reverse([37,2,5,1,-9]))
print(reverse([37,2,10,5,1,-9]))