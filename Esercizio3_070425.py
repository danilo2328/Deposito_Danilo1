#creazione variabili
nome = ""
password = ""
id = 0
x = True

#registrazione
if x:
    nome = input("inserisci un nickname ")
    password = input("inserisci la tua password ")
    id +=1

#login
if nome == "":
    print("non hai valorizzato")
else:
    nome_inserito = input("inserisci un nickname ")
    password_inserito = input("inserisci la tua password ")
    
    if nome_inserito == nome and password_inserito == password:
        print("sei loggato")