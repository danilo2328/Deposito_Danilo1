import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Genitore1', 'Genitore2', 'Genitore3'],
'Età': [25, 30, 24],
'Città': ['Roma', 'Milano', 'Torino']
}
df = pd.DataFrame(data)

# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

# Selezione delle righe dove l'età è superiore a 23
df_older = df[df['Età'] > 23]

# Stampa delle righe selezionate
print("\nPersone con età superiore a 23 anni:")
print(df_older)

# Aggiungiamo una nuova colonna la persona maggiorenne
df['Maggiorenne'] = df['Età'] >= 18
df['Minore di 30'] = df['Età'] < 30
df['Milano'] = df['Città'] == 'Milano'

# Stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne':")
print(df) 