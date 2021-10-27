# Kata Basic Python

# Funcion quicksort
"""
Funcion para ordenacion rapida
"""

def quicksort(a, inf, sup):
    i = inf 
    j = sup
    x = a[int((inf+sup) / 2)]

    while i <= j:
        while a[i]<x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <=j:
            tam = a[i]
            a[i] = a[j]
            a[j] = tam
            i +=1
            j -=1
    if inf < j:
        quicksort(a,inf,j)    
    if i < sup:
        quicksort(a,i,sup)


array = [99,85,1,20,4,87,32,65,34,38,7,55,22,49,51]

print (array)
quicksort(array,0,len(array)-1)
print (array)
