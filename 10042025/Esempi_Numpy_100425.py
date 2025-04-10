import numpy as np

#-------------------------- SLIDE 212 - LINSPACE: numeri equidistanti tra un range di dati (il range è compreso)
import numpy as np

arr1= np.linspace(10, 50, 5)
print(arr1)

arr = np.linspace(0, 1, 5)
print(arr) # Output: [0. 0.25 0.5 0.75 1. ]


#-------------------------- SLIDE 212 - RANDOM: genera numeri casuali
import numpy as np

random_arr = np.random.rand(3, 3)

random_arr1 = np.random.rand(2,2)

# Matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)
print(random_arr1)


#-------------------------- SLIDE 213 - SUM, MEAN, STD

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)
print("Sum:", sum_value) # Output: Sum: 15
print("Mean:", mean_value) # Output: Mean: 3.0
print("Standard Deviation:", std_value) # Output: Standard Deviation: 1.4142135623730951