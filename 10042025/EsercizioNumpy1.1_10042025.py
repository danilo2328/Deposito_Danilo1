#--------------------- Creare una Classe e delle funzioni

import numpy as np

class OperazioniArray:
    def __init__(self):
        self.arr_equi = None
        self.arr_cambiaforma = None
        self.arr_numericasuali = None
    
    def crea_array_equidistante(self, start=0, stop=1, num=12):
        self.arr_equi = np.linspace(start, stop, num)
        print("\nArray equidistante:")
        print(self.arr_equi)
        
    def cambia_forma(self, righe, colonne):
        self.arr_cambiaforma = self.arr_equi.reshape(righe, colonne)
        print("\nArray Cambia Forma")
        print(self.arr_cambiaforma)
        
    def array_casuale(self, righe, colonne):
        arr_numericasuali = np.random.rand(righe, colonne)
        print("\n Array Casuale")
        print(arr_numericasuali)
        
    def somma_array(self):
        sum_value1 = np.sum(self.arr_equi)
        sum_value2 = np.sum(self.arr_numericasuali)
        print("\n Somma Elementi")
        print(sum_value1)
        print(sum_value2)
        

op = OperazioniArray()
op.crea_array_equidistante()
op.cambia_forma(3, 4)
op.array_casuale(3, 4)
op.somma_array()