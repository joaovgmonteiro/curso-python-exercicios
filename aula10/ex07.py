import pandas as pd

df = pd.read_excel('bancos.xlsx')
filtro = df[df['Banco'] == 'Banco do Brasil']
#print(df)
print(filtro)