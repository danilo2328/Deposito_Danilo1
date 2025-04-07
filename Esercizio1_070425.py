#esercizio if
numero = int(input("inserisci un valore intero maggiore di 10"))
if numero > 10:
    numero = int(input("inserisci un valore intero maggiore di 20"))
    if numero > 20:
        print("hai scelto un valore maggiore di 20")
    else:
        print("hai sceto un valore minore di 20")
else:
    print("hai inserito un valore inferiore a 10")