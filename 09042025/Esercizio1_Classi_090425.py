import math

#Crea una classe chiamata Punto. Questa classe dovrebbe avere 2 attributi x e y che rappresentano le coordinate

class Punto:
    def __init__(self, x ,y ):
        self.x = x
        self.y = y
    
#Un metodo che prenda in input un valore per dx e un valore per dy e ne modifiche le coordinate

    def modifica_coordinate (self):
        dx = int(input("inserisci un valore per x "))
        dy = int(input("inserisci un valore per y "))
        self.x += dx
        self.y += dy

#un metodo distanza da origine che restituisca la distanza dal punto 0,0 del piano

    def distanza_origine(self):
        print("la distanza dall'origne 0,0 è ", math.sqrt(self.x**2+self.y**2))

#output
p = Punto(2,2)
p.distanza_origine()
p.modifica_coordinate()
p.distanza_origine()