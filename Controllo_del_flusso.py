#condizione con i numeri
numero = int(input("inserisci un numero intero "))
if numero > 11:
    print("il numero è maggiore di 11")
elif numero == 11:
    print("il numero è uguale a 11")
else:
    print("il numero è minore di 11")
    
    
#condizione con le stringhe
stringa = "dan"
if stringa.lower() == "casa":
    print("wow")
else:
    print("non")