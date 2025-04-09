import pandas as pd

#importare file nella stessa cartella 

# Percorso del file CSV
file_path = 'vendite.csv' #se cartella diversa inserire tutto il percorso file

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare
print(df.head())