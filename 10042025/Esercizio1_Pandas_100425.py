import pandas as pd
import numpy as np

# Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su un gruppo di persone: Nome, Età, Città e Salario.
# Caricare i dati in un DataFrame autogenerandoli casualmente

data = {
'Nome': ['Alice', 'Bob', 'Carla', 'D', 'Carla', 'P', None],
'Età': [25, 30, 22, 30, np.nan, 25, 29],
'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma'],
'Salario': [20, 25, 30, 35, 40, 45, 50]
}
df = pd.DataFrame(data)
print("\nDataFrame Originale")
print(df)


# Visualizzare le prime e le ultime cinque righe del DataFrame
print("\nPrime 5 righe")
print(df[0:5])
print("\nUltime 5 righe")
print(df[-5:])

# Visualizzare il tipo di dati di ciascuna colonna
print("\nVisualizza tipo dato", df.dtypes)

# Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard)
print("\nEtà Media", df['Età'].mean())
print("\nEtà Mediana", df['Età'].median())
print("\nEtà std", df['Età'].std())

print("\nSalario medio", df['Salario'].mean())
print("\nSalario mediano",df['Salario'].median())
print("\nSalario std",df['Salario'].std())

# Identificare e rimuovere eventuali duplicati
df1 = df.drop_duplicates()
print("\nDati senza duplicati")
print(df1)

# Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna
df['Età'].fillna(df['Età'].median(), inplace=True)
print("\nSostiture con la mediana")
print(df)

# Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
# anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
df['Giovane'] = df['Età'] < 19
df['Adulto'] = (df['Età'] >= 19) & (df['Età'] <= 65)
df['Senior'] = df['Età'] > 65

# Salvare il DataFrame pulito in un nuovo file CSV.
