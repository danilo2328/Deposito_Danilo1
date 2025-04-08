#Slide 81 - Punto3
#Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato diciascun numero nella lista.

print("calcoliamo il quadrato dei numeri interi, inserisci 3 numeri")
x = int(input("inserisci il primo numero intero "))
y = int(input("inserisci il secondo numero intero "))
z = int(input("inserisci il terzo numero intero "))

#calcolare e stampare il quadrato dei numeri selezionati 
lista = [x, y, z]
lista2 = [x*x, y*y, z*z]
print("il quadrato dei numeri inseriti è", lista2)
