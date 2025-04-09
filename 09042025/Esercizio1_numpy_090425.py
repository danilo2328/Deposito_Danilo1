import numpy as np

#Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50

arr = np.random.randint(10,50,20)
print(arr)

#Utilizza lo slicing per estrarre i primi 10 elementidell'array
print(arr[0:10])

#Utilizza lo slicing per estrarre gli ultimi 5 elementidell'array.
print(arr[-5:])

#Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
print(arr[5:15])

#Utilizza lo slicing per estrarre ogni terzo elementodell'array
print(arr[0:20:3])

#Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
arr1 = arr
arr1[5:10] = 99
print(arr1)

arr_modificato = np.array(arr)
arr_modificato [5:10] = 99
print(arr_modificato)