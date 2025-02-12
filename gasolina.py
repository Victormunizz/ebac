import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina = "gasolina.csv"
df = pd.read_csv(gasolina)

(df.head())

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df, x='dia', y='venda', palette = "pastel" )
  grafico

  plt.savefig("gasolina.png")