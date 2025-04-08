#slide 97 esercizio 1

import random

def indovina_il_numero():
    numero_da_indovinare = random.randint(0, 100)
    while True:
        numero_inserito = int(input("inserisci un numero intero tra 0 e 100 inclusi: "))
        if numero_da_indovinare == numero_inserito:
            print("hai indovinato")
            break
        elif numero_inserito < numero_da_indovinare:
            print("numero inserito è più basso di quello da indovinare")
            scelta = input("Vuoi riprovare? SI/NO ").upper()
            if scelta == "SI":
                continue
            else:
                print("Game Over")
                break
        elif numero_inserito > numero_da_indovinare:
            print("numero inserito è più alto di quello da indovinare")
            scelta = input("Vuoi riprovare? SI/NO ").upper()
            if scelta == "SI":
                continue
            else:
                print("Game Over")
                break
            
            
indovina_il_numero()