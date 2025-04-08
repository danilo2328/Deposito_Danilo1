#Slide 97 esercizio 2

def sequenza_fibonacci():
    numero = int(input("Inserisci un numero: "))
    a = 0 
    b = 1
    print("La sequenza di Fibonacci fino ad ", numero, "è: ")
    while a <= numero:
        print(a)
        a = b 
        b = a + b
        
        
sequenza_fibonacci()