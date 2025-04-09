#Crea una classe chiamata libro con 3 attributi: titolo autore e pagine
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

#Crea un metodo descrizione che restituisca una stringa "il libro è titolo, scritto da autore, con pagine"

    def descrizione_libro(self):
        print("Il libro si intitola", self.titolo ,"è scritto da", self.autore ,"il totale delle pagine è ", self.pagine)


#output
libro1 = Libro("A", "B", 12)
libro1.descrizione_libro()