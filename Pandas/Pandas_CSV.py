import displayfunction
import pandas as pd
import plotly.express as px

# IMPORT

tabela = pd.read_csv('telecom_users.csv')

# TRATAR, DELETAR DADOS INUTEIS
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all",axis=1)
tabela = tabela.dropna(how="any",axis=0)

# VER DADO RELEVANTE, ANALISE EXPLORATORIA

# display(tabela["Churn"].value_counts())
# display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# PLOT

# for coluna in tabela.columns:
#     print(coluna)
#     grafico = px.histogram(tabela, x=coluna, color="Churn")
#     grafico.show()
