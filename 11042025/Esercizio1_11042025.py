import sqlite3  # Importa il modulo per lavorare con SQLite

#Crea un database SQLite chiamato scuola.db.

risposta_Db = input("vuoi inserire un nuovo DB scolastico? SI/NO ").upper()
if risposta_Db == "SI":
    nome_DB = input("Scrivi il nome del DB").upper()
    database = 0
    j = 1
    if j < 2:
        conn = sqlite3.connect(nome_DB)
        cur = conn.cursor()
        print("\nHai creato il database", nome_DB)
    else:
        print("\nDatabase presente")


#Crea una tabella chiamata studenti con i campi id (intero, chiave primaria) e nome (testo).

    cur.execute('''
        CREATE TABLE IF NOT EXISTS nome_DB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    ''')

    #Menù che Inserisce studenti con nomi a tua scelta

    while True:
        scelta = input("\nvuoi inserire un altro studente? SI/NO ").upper()
        if scelta == "SI":
            nome = input("\ninserisci il nome dello studente ")
            cur.execute("INSERT INTO nome_DB (nome) VALUES (?)", (nome,))
            print("\nhai aggiunto un nuovo studente")
        else: 
            break

    print("\nla lista degli studenti è: ")
    cur.execute('''
                SELECT * 
                FROM studenti
                ''')
    righe = cur.fetchall()
    for riga in righe:
        print(riga)

else:
    print("Nessun DB creato")
    
#conn.close()