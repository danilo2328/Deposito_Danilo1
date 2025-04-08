#slide 80

print("questo sarà un countdown")
while True:
    numero = int(input("Inserisci un numero intero < 10 "))
    if numero < 10:
        for i in range(numero, 0, -1):
            print (i)
    else:
        print("numero non valido")
        break
    scelta = input("vuoi continuare? SI/NO ").upper()
    if scelta == "SI":
        continue
    if scelta == "NO":
        print("countdown concluso")
        break
    else:
        print("risposta non valida, programma concluso")
        break