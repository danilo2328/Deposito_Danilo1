import numpy as np 

# Creazione di un array unidimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2d)

# Creazione di un array 3.
arr = np.array([1, 2, 3, 4, 5])

#---------------------------------------------------- SLIDE 197

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr2d.ndim) # Output: 1
print("Tipo di dati:", arr2d.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr2d.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

#------------------------------------------------------ SLIDE 199

import numpy as np 
arr = np.arange(10)
print(arr) # Output: [0 1 2 3 4 5 6 7 8 9]

import numpy as np
arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr) # Output: [[0 1 2] [3 4 5]]


#---------------------------------------------------- SLIDE 200

import numpy as np 

#Utilizza la funzione np.arange per creareun array di numeri interi da 10 a 49
arr = np.arange(10,50)
print(arr)

#Verifica il tipo di dato dell'array estampa il risultato
print("Tipo di dati:", arr.dtype)

#Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo didato
arr1 = np.array(arr, dtype="float64")
print("Tipo di dati:", arr1.dtype)

#stampa la forma dell'array
print("Forma dell'array:", arr.shape)

#-------------------------------------------------------- SLIDE 201

import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
arr2d = np.array([1,2,3], [4,5,6])

# Indexing --> indicare il punto
print(arr[0]) # Output: 1

# Slicing --> estrarre
print(arr[1:3]) # Output: [2 3]

# Boolean Indexing --> 
print(arr[arr > 2]) # Output: [3 4 5]

#-------------------------------------------------------- SLIDE 202

import numpy as np 

arr2d = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
print(arr2d)

# Slicing sulle righe, elimina la riga 1, prende solo la riga 2 e 3
print(arr2d[1:3]) # Output: [[ 5 6 7 8] [ 9 10 11 12]]

# Slicing sulle colonne, la colonna 3 viene esclusa quindi prende solo la colonna 1 e 2
print(arr2d[:, 1:3]) # Output: [[ 2 3] [ 6 7] [10 11]]

# Slicing misto
print(arr2d[1:, 1:3]) # Output: [[ 6 7] [10 11]]


#-------------------------------------------------------- SLIDE 203

import numpy as np 

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base --> posizione 2 compresa, posizione 7 esclusa
print(arr[2:7]) # Output: [2 3 4 5 6]

# Slicing con passo
print(arr[1:8:2]) # Output: [1 3 5 7] --> posizione 1 compresa, posizione 8 esclusa, passo 2

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4] --> posizione 0 compresa, posizione 5 esclusa
print(arr[5:]) # Output: [5 6 7 8 9] --> posizione 5 compresa, posizione 9 compresa

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]

#-------------------------------------------------------- SLIDE 205

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices]) # Output: [20 40] --> posizione 1 e posizione 3

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices]) # Output: [10 30 50] --> posizione 0, 2 e 4