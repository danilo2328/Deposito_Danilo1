#lettura file
file = open("esempio_testo.txt", "r")

tutte_le_righe = file.read()
riga = file.readline()

print(tutte_le_righe)

file.close()

#sovrascrittura file (se il file non esiste ne crea uno nuovo)
file = open("esempio_testo.txt", "w")

file.write("Sto sostituendo il testo")
file.close()


#utilizzando il with, la chiusura è automatica
with open("esempio_testo.txt", "r") as file:
    contenuto = file.read()
