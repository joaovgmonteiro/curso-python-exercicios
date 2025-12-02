import pandas as pd

data_frame = pd.read_csv('ClassicDisco.csv')

# Filtrar música lançadas após 1980
#print(data_frame[data_frame['Year'] > 1980])

print(data_frame[data_frame['Year'] > 1980][['Year', 'Track']]) 