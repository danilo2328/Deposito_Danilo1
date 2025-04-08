#slide 80 - numero pari
print("Il tuo numero è un numero pari?")
numero = int(input("Inserisci un numero intero "))
if numero%2==0:
    print(numero, "è un numero pari")
else:
    print(numero, "è un numero dispari")
    
    
    
#slide 80 - numero primo

print("Il tuo numero è un numero primo?")
numero = int(input("Inserisci un numero intero "))
numeroprimo = True
for i in range(2,numero):
    if numero%i==0:
        numeroprimo = False
        if numeroprimo:
            print(numero, "è un numero primo")
        else:
            print(numero, "non è un numero primo")