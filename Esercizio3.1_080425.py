#Slide 81 - Punto1
# Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari e "Dispari" se il numero è dispari.

print("Il tuo numero è un numero pari?")
numero = int(input("Inserisci un numero intero "))
if numero%2==0:
    print(numero, "è un numero pari")
else:
    print(numero, "è un numero dispari")