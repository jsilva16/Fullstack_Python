import random
def randInt(min=0, max=100):
    neg=1
    if max < 0:
        neg= -1
    elif min>max:
        temp=min
        min=max
        max=temp
    num=min
    while num>max or num<=min:
        num = random.random()
        num = int(num*1000)
        num=num*neg
        if neg == -1 and num<0 and num>min:
                print('El número aleatorio entre 0 y',min,'es:',num)
                return num
        elif num>=min and num<=max:
            
            print('El número aleatorio entre',min,'y',max,'es:',num)
            return num
randInt(50,-500)

#////////////////////////////////////////////////////////////////////////

#LOTO

def randInt(min=0, max=100):
    neg=1
    if max < 0:
        neg= -1
    if min>max:
        temp=min
        min=max
        max=temp
    num=min
    while num>max or num<=min:
        num = random.random()
        num = int(num*1000)
        num=num*neg
        if neg == -1 and num<0 and num>min:
            return num
        elif num>=min and num<=max:
            return num
randInt(2,60)

def loto():
    card=[]
    for i in range (5):
        row=[]
        for j in range (4):
            num2=randInt(0,99)
            row.append(num2)
        card.append(row)
    return card
print(loto())

#print(randInt()) 		    # debería imprimir un número aleatorio entre 0 a 100
#print(randInt(max=50)) 	    # debería imprimir un número aleatorio entre 0 a 50
#print(randInt(min=50)) 	    # debería imprimir un número aleatorio entre 50 a 100
#print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500