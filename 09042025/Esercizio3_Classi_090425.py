#Crea una classe biblioteca che permette di creare un libro e stamparlo

#Classe libro
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        print("Il libro si intitola", self.titolo ,"è scritto da", self.autore ,"il totale delle pagine è ", self.pagine)

#Aggiungere libro alla classe biblioteca
class Biblioteca:
    def __init__(self, libri_presenti):
        self.libri_presenti = []
        
    def aggiungi_libri(self):
        titolo = input("inserisci il titolo")
        autore = input("inserisci l'autore")
        pagine = input("inserisci il numero di pagine")
        self.nuovo_libro = Libro(titolo, autore, pagine)
        
    def descrizione_biblioteca(self):
        if self.libri_presenti:
            self.libri_presenti.descrizione()
        else:
            print("nessun libro presente")
            
b = Biblioteca()
b.aggiungi_libri()
b.descrizione_biblioteca()