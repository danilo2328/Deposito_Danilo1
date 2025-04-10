import numpy as np

class OperazioniArray2:
    def __init__(self):
        self.arr_equi = None
        self.arr_numericasuali = None
        self.arr_sommaelementi = None
        self.arr_sommatotale = None
        self.arr_sommamaggiori5 = None
        
    def array_equidistante(self, start=0, stop=10, num=50):
        self.arr_equi = np.linspace(start, stop, num)
        print("\nArray equidistante:")
        print(self.arr_equi)
        
    def array_casuale(self, num):
        self.arr_numericasuali = np.random.rand(num)
        print("\nArray Casuale")
        print(self.arr_numericasuali)
        
    def somma_elementi(self):
        self.arr_sommaelementi = self.arr_equi + self.arr_numericasuali
        print("\nSomma elementi")
        print(self.arr_sommaelementi)
        
    def somma_totale(self):
        self.arr_sommatotale = np.sum(self.arr_equi) + np.sum(self.arr_numericasuali)
        print("\nSomma Totale")
        print(self.arr_sommatotale)
        
    def somma_maggiore_di_5(self):
        self.sommamaggiore5 = np.sum(self.arr_sommaelementi[self.arr_sommaelementi > 5])
        print("\nSomma maggiore di 5")
        print(self.sommamaggiore5)
        
        
op = OperazioniArray2()
op.array_equidistante()
op.array_casuale(50)
op.somma_elementi()
op.somma_totale()
op.somma_maggiore_di_5()
        
    