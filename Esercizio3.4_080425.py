#Slide 81 - Punto4
#Scrivi un sistema che prende in input una lista di numeri interi che precedente è stata valorizzata dall’utente. Il sistema deve:
#Utilizzare un ciclo for per trovare il numero massimo nella lista. 1.
#Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista. 2.
#Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.

print("calcoliamo il quadrato dei numeri interi, inserisci 3 numeri")
x = int(input("inserisci il primo numero intero "))
y = int(input("inserisci il secondo numero intero "))
z = int(input("inserisci il terzo numero intero "))

lista = [x, y, z]

#individuare il max
max1 = max(lista)
print("il numero più grande tra quelli inseriti è ", max1)

#individuare il max con ciclo for
max2 = 0
for i in lista:
    if x > max2:
        max2 = x
print("il massimo è ", max2)

#conta i valori in lista con ciclo while
contatore = 0
i = 0
while i < len(lista):
    contatore +=1
    i +=1
print("All'interno della lista ci sono ", contatore, " numeri")

#condizione if per lista vuota, altrimenti numero valori e max valore

risposta = input("vuoi inserire una lista? SI/NO ").upper()
if risposta == "SI":
    x = int(input("inserisci il primo numero intero "))
    y = int(input("inserisci il secondo numero intero "))
    z = int(input("inserisci il terzo numero intero "))
    lista = [x, y, z]
    
    contatore = 0
    i = 0
    while i < len(lista):
        contatore +=1
        i +=1
    print("All'interno della lista ci sono ", contatore, " numeri")
    
    max1 = max(lista)
    print("il numero più grande tra quelli inseriti è ", max1)
        
else:
    print("Lista Vuota")
        
    