arra = [5,3,4,9,8,6,1,7,0]

def insert_ord(arr):
    for i in range (1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr.insert(j-1,arr[i])
                print("ins",arr)
                arr.pop(i+1)
                print("remove",arr)
            j-=1
    return arr
insert_ord(arra)



#Definiendo la funcion
def ordenarInsercion(lista):
    for i in range(1, len(lista)):
        for j in range(i,0,-1):
            if lista[j-1]>lista[j]:
                auxiliar = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = auxiliar
    return lista

print(ordenarInsercion([5,8,3,6,4,9,10]))





def insertSort(arr):
	for i in range(1,len(arr)):
		x=i
		while (arr[i]<arr[x-1]) and x>0 :
			x-=1
		temp=arr[i]
		arr.pop(i)
		arr.insert(x,temp)

	return arr

print(insertSort(arra))
