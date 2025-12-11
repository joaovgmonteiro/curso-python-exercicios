from sqlalchemy import create_engine

import pandas as pd

# Parametros de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'aulapandas'

# criação da engine de conexão
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# leitura da tabela
df = pd.read_sql("SELECT * FROM odontologia", con=engine)
print(df)