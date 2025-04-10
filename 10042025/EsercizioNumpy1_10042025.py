import numpy as np

#Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace

arr= np.linspace(0, 1, 12)
print(arr)

#Cambia la forma dell'array a una matrice 3x4.
reshaped_arr = arr.reshape((3, 4))
print("\nCambia forma")
print(reshaped_arr)

#Genera una matrice 3x4 di numeri casuali tra 0 e 1.
random_arr = np.random.rand(3, 4)
print("\nGenera numeri Casuali")
print(random_arr)

#Calcola e stampa la somma degli elementi di entrambe le matrici.
sum_value1 = np.sum(arr)
sum_value2 = np.sum(random_arr)
print("\nSomma elementi")
print(sum_value1)
print(sum_value2)