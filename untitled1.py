#Importando biblioteca pandas

import pandas as pd

dados_origem = pd.read_csv('dados_carros.csv')

df = dados_origem

df

df.head() #Mostra as primeiras quatro linhas

df.tail() #Mostra as últimas quatro linhas

df.tail(3) #Vai mostrar apenas os três últimos da cauda

df.describe() #Mostra algumas estatísticas básicas, std = desvio padrão, o quão longe está da média seus itens.

df.info() #Mostra a quantidade de não nulos, e o seu tipo, se são objetos, inteiros e etc.

valores = pd.Series([30,40,60,70,90,25,32])

valores #É um dataframe criado pelo pandas, com uma coluna sendo o índice, e a outra coluna sendo os valores
# Com o tipo int64

valores.mean() #A média dos valores do dataframe

valores.sum() #Soma dos valores

valores.std() #Desvio padrão dos valores

valores.median() #Mediana dos valores

df['Fabricante'] #Mostra só uma coluna especificada do Dataframe, e é case sensitive

df['Preco'].mean() #Mostra a média da coluna preco

df['Preco'].max() #Mostra o valor máximo da coluna preco

df['Cor'] == 'Azul' #Mostra com true ou false, na coluna cor, a onde é true e onde é falso

df[df['Cor'] == "Azul"] #Agora só mostra as linhas que a cor é azul

df['Quilometragem']<50000 #Vai mostrar as colunas com true ou false que forem menores que 50.000
#caso queira mostrar quais linhas tem isso, você pode colocar df[df['Quilometragem']<50000]

df[df['Quilometragem']<50000]

df[df['Preco']>=100000] #Carros com valor maior que 100.000

df[df['Fabricante'] == 'Honda'] #Carros da Honda

df[df['Fabricante'].isin(["Toyota", "Honda"])] #Carros da Honda e Toyota

df[~df['Fabricante'].isin(["Toyota", "Honda"])] #Negação, ou seja, pega o que não é toyota ou honda

df2 = pd.read_csv('dados_faltando.csv')

df2 #Mostra o dataframe do df2

df2.info()

df2['Quilometragem'].fillna(df2['Quilometragem'].mean(), inplace=True) #Substitui os valores nulos pela média
#Se não tivesse o inplace=True, teria que colocar df2['Quilometragem'] = a linha acima
#Com o inplace já entende que vai atualizar a própria coluna

df2.info()

df2

df2.dropna(subset = ['Portas'], inplace = True) #Dropa as linhas que tiverem NaN

df2

df['Preco'].fillna(df2['Preco'].mean(), inplace=True) #Coloca a média a onde é nulo no preco

df2['IPVA'] = df2['Preco'] * 0.04 #Cria uma nova coluna no dataframe com um campo calculado

df2

df2['Motor'] = "1.0" #Cria uma nova coluna motor, cujo todos os valores são 1.0