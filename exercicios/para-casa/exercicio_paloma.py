# Utilizar a tabela de dados do clima de seu estado, manipule os dados de acordo com as instruções abaixo: 
# Utilizei a planilha do debate - Bonito 

import pandas as pd

df = pd.read_csv('ON35-S11-PLANILHA.CSV', delimiter=';', skiprows=8, encoding='latin1')

df.head()

# - calcular a média da temperatura da amostra 

coluna_temperatura = df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)']

coluna_temperatura = pd.to_numeric(df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'], errors='coerce')

coluna_temperatura.mean()

# - retirar nulos da coluna 'RADIACAO GLOBAL (Kj/m2)' # substituir por PRECIPITAÇÃO TOTAL, HORÁRIO (mm)

df_sem_nulos_colunas = df.dropna(axis=1)

# - copiar o dataframe reduzindo para 3 colunas (a sua escolha) e 1000 linhas (aleatórias) 

df_reduzido = df[['Data', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']]

df_reduzido.head()

amostra = df.sample(n=1000)

# - Bônus: normalizar coluna (qualquer uma) 

df['Coluna1_normalizada'] = (df['UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)'] - df['UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)'].min()) / (df['UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)'].max() - df['UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)'].min())

# - Bônus II: pesquisar sobre outras formas de processamento de dados além das vistas em sala de aula


