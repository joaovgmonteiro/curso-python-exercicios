'''
Exercício: Manipulação de arquivos csv com Pandas -> Filtrar colunas
Você foi contratado para analisar uma planilha de músicas chamada ClassicDisco.csv, contendo informações sobre músicas clássicas
de discoteca, com as seguintes colunas:
. Artista(Artist)
. Musica(Track)
. Ano(Year)
. Album(Album)
Seu objetivo é explorar os dados usando diferentes métodos da biblioteca Pandas.
'''

import pandas as pd 

data_frame = pd.read_csv("ClassicDisco.csv")


#filtro = data_frame['Artist']

#filtro = data_frame['Track']

#filtro = data_frame['Year']

filtro = data_frame['Album']
print(filtro)