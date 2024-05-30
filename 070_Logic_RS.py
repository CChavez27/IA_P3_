def countingSort(arr, expl): 
    n = len(arr) 
    output = [0] * (n)
    count = [0] * (10)  #Arreglo del los 10 digitos del Sis num

    for i in range(0, n): 
        index = arr[i] // expl  #Extraemos el digito de la unidad dividiendo Ej 3456/10 = 345
        count[index % 10] += 1  #Hacemos una operacion de modulo % para extraer el ultimo digito 345%10=5

    #Preprocesamos el arreglo de conteo de ese digito 
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // expl
        output [count [index % 10]- 1] = arr[i] 
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr) #Encontramos el elemento mas grande

    exp = 1
    while max1 / exp >= 1:      #Por cada digito que se tiene
        countingSort(arr, exp)  #Se ejecuta CS
        exp *= 10

 
# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
 
# Function Call
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i],end=" ")
