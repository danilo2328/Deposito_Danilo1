import numpy as np

#Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
arr= np.linspace(0, 10, 50)
print("\nArray di 50 numeri equidistanti tra 0 e 10")
print(arr)

#Utilizza np.random.random per creare un array di 50 numeri casuali compresitra 0 e 1.
random_arr = np.random.rand(50)
print("\nArray di 50 numeri casuali tra 0 e 1")
print(random_arr)

#Somma i due array elemento per elemento per ottenere un nuovo array.
somma_elementi = arr + random_arr
print("\nArray somma elemento per elemento")
print(somma_elementi)

#Calcola la somma totale degli elementi del nuovo array
somma_array1 = np.sum(arr)
somma_array2 = np.sum(random_arr)
somma_totale = somma_array1 + somma_array2
print("\nSomma totale Array")
print(somma_totale)

#Calcola la somma degli elementi del nuovo array che sono maggiori di 5
somma_maggiori5 = np.sum(somma_totale[somma_totale > 5])
print(somma_maggiori5)