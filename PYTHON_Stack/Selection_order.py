arra = [5,3,4,9,8,6,1,7,0]

def selectSort(arr):
    ind=0
    for j in range (len(arr)-1):
        min=arr[j]
        min_index=j
        for i in range (j+1,len(arr)):
            if arr[i]<min:
                min_index=i
                min=arr[i]    
        #arr[j],arr[min_index]=arr[min_index],arr[j]
        temp=arr[ind]
        arr[ind]=arr[min_index]
        arr[min_index]=temp
        ind+=1
    return arr

selectSort(arra)

