import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./DADOS/trees.csv')
mostra = dataset.head()

print(mostra)

circ = dataset.Girth
altura = dataset.Height
volume = dataset.Volume

plt.figure(1)

plt.subplot(2,2,1)
plt.scatter(circ, volume)

plt.subplot(2,2,2)
plt.scatter(circ, altura)

plt.subplot(2,2,3)
plt.scatter(volume, altura)