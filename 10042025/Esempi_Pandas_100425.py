import pandas as pd

# Percorso del file CSV
file_path = 'vendite.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare
print(df.head())


#--------------------------------------------SLIDE 238

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


#--------------------------------------------SLIDE 241

import pandas as pd
import numpy as np

# DataFrame esempio, inclusi valori mancanti e duplicati
data = {
'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
'Età': [25, 30, 22, 30, np.nan, 25, 29],
'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}
df = pd.DataFrame(data)

# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

# Rimozione dei duplicati
df = df.drop_duplicates()

# Gestione dei dati mancanti
# Rimozione delle righe dove almeno un elemento è mancante
df_cleaned = df.dropna()

# possiamo sostituire dati mancanti con valore di default
df['Età'].fillna(df['Età'].mean(), inplace=True)

# Stampa del DataFrame pulito
print("\nDataFrame dopo la pulizia:")
print(df_cleaned)

# Stampa del DataFrame con dati mancanti sostituiti
print("\nDataFrame con dati mancanti sostituiti:")
print(df)