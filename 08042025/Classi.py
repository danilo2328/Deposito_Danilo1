class Penna():
    altezza = 0
    larghezza = 0
    
    #metodo speciale: costruttore
    def __init__(self, h, l):
        self.altezza = h
        self.larghezza = l
        
oggetto_penna = Penna(10,7)

print(oggetto_penna.larghezza)
print(oggetto_penna.altezza)



class Guerriero():
    altezza = 0
    peso = 0
    acconciatura = 0
    
    def __init__(self, h, p, a):
        self.altezza = h
        self.peso = p
        self.acconciatura = a
        
oggetto_Guerriero = Guerriero(175, 75, 2)
print(oggetto_Guerriero.altezza)
print(oggetto_Guerriero.peso)
print(oggetto_Guerriero.acconciatura)