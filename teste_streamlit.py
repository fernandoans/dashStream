# -*- coding: utf-8 -*-
"""Teste-Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gwkH-4At3FrUqwcCfEXQtXzZJCD-wEcn

# **Definição das Bibliotecas**
"""
!pip install psycopg2

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""# **Conexão com o Banco de Dados DATA_IESB**"""

try:
    conn = psycopg2.connect(
      dbname="Data_IESB",
      user="Data_IESB",
      password="DATA_IESB",
      host="dataiesb.iesbtech.com.br",
      port="5432"
    )
    print("Conexão bem-sucedida!")
except psycopg2.Error as e:
    print("Erro ao conectar ao PostgreSQL:", e)

cur = conn.cursor()

"""# **Leitura de uma view do Banco de Dados**"""

view_populacao = pd.read_sql_query("SELECT * FROM Brasil_Populacao", conn)

conn.close()

"""# **Exemplo de criação de um gráfico usando uma visão do banco de dados**"""

populacao_por_regiao = view_populacao.groupby('nome_regiao')['numero_habitantes'].sum().reset_index()

fig_regiao = px.bar(populacao_por_regiao,
                    x='nome_regiao',
                    y='numero_habitantes',
                    labels={'nome_regiao': 'Nome da Região', 'numero_habitantes': 'Número de Habitantes'},
                    title='População por Região')
fig_regiao.show()
