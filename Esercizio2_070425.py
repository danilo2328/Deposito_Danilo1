#esercizio lista - aggiungi, rimuovi, elimina
lista1 = ["d", "a", "n", "i", "l", "o"]
scelta = int(input("scegli cosa vuoi fare: 1 elimina, 2 aggiungi o 3 modifica? "))

if scelta == 1:
    print(lista1)
    scelta1 = str(input("inserisci la lettera da eliminare "))
    lista1.remove(scelta1)
    print(lista1)
elif scelta == 2:
    print(lista1)
    scelta2 = str(input("inserisci una lettera "))
    lista1.append(scelta2)
    print(lista1)
elif scelta == 3:
    print(lista1)
    lettera3 = int(input("inserisci la posiizione della lettera da modificare "))
    lettera4 = str(input("inserisci una nuova lettera "))
    lista1[lettera3] = str(lettera4)
    print(lista1)
else:
    print("seleziona 1 elimina, 2 aggiungi o 3 rimuovi")