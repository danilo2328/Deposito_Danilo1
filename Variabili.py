#variabile numerica - Tipo numerico
intero = int(5)
decimale = float(3.3)

print (intero, "e" , decimale)

#variabile stringa - Tipo semantico
stringa1 = input("inserisci una parola")

#metodi sulle stringhe
s = "donde esta la bilbioteca"
print(len(s))
print(s.upper())
print(s.split())
print(s.replace("bilbioteca", "plaza"))

#variabili Booleani
x = len("abc")
y = len("Daniloooo")
z = 7
print(x < y and y > z)
print(not(x < y))