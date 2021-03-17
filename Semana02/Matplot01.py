import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

### Gráfico básico

x = [1,2,3,4]
y = [0,2,4,6,8]

# Redimensionamento do gráfico
plt.figure(figsize=(5,3), dpi=100)


# Configura de uma forma muito grande
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

#Configura a cor , tipo de linha
plt.plot(x,y, 'b^--', label='2x', )


# Seleciona o intervalo
x2 = np.arange(0,4.5,0.5)

# Plota o gráfico x2
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

# Plota o que faltou do gráfico
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Adiciona titulo e formata tipo de letra, tamanho
plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# Nome dos eixos
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Escala do gráfico
plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# Adiciona legenda
plt.legend()

# Salva a figura
plt.savefig('mygraph.png', dpi=300)

# Plota o gráfico
plt.show()