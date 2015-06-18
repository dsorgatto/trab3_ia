from numpy import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# funcao para calculo da distancia euclidiana
def calc_dist(a, b, c, d):
    dist = math.sqrt(((a-b)**2)+((c-d)**2))
    return dist

#abre o arquivo e o converte em dois vetores X e Y
arquivo = pd.read_csv("artificial_2.data", header=None, sep=',')
valores = arquivo.iloc[:,:2]
matrix = valores.as_matrix()
x=[]
y=[]
for px, py in matrix:
    x.append(px)
    y.append(py)

#Valor de K para esse dataset
k = 2    

#forma o grafico dos dados antes da classificacao
plt.clf()
plt.scatter(x, y, alpha=0.5, c='green')
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Antes de classificar')
plt.savefig('antes.png')

sse = []
for z in range(10):
    #cria os pontos de cluster
    pontos = []
    np.random.seed(z*2)
    for i in range(k):
        pX = list(np.random.normal(np.mean(x), np.std(x), 1))
        pY = list(np.random.normal(np.mean(y), np.std(y), 1))   
        pontos.append([pX, pY])
    
    #controla as iteracoes
    for itera in range(1, 11):
        indices = []
        for i in range(len(x)):
            distancia = []
            for j in range(len(pontos)):
                distancia.append(calc_dist(x[i], pontos[j][0], y[i], pontos[j][1]))
            indices.append(distancia.index(min(distancia)))
        
        #cria os cluster e os povoa
        cluster = []
        for i in range(k*2):
            cluster.append([])
        m = 0
        for j in range(len(pontos)):
            for i in range(len(indices)):
                if indices[i] == j:
                    cluster[m].append(x[i])
                    cluster[m+1].append(y[i])
            m += 2
        #gera o grafico dos clusters
        titulo = "Iteracao {} com {} pontos".format(itera, k)
        saver = "depois_{}.png".format(itera)
        cores = ['b', 'r', 'y', 'g', 'c', 'm', 'k', '0.75', '0.5', '0.25']
        plt.clf()
        j = 0
        for i in range(0, k*2, 2):
            plt.scatter(cluster[i], cluster[i+1], alpha=0.5, c=cores[j])
            plt.scatter(pontos[j][0], pontos[j][1], s=100, c=cores[j], alpha=0.2)
            j += 1
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.title(titulo)
        plt.savefig(saver)
        
        #calcula as medias e atualiza os pontos
        j = 0
        for i in range(k):
            if len(cluster[i*2])> 0:
                pontos[i][0] = np.mean(cluster[j])
                j += 1
                pontos[i][1] = np.mean(cluster[j])
                j += 1
    
    #calculo da Soma do Erro Quadratico
    valor = 0.0
    m = 0
    for j in range(k):
        for i in range(len(cluster[m])):
            valor += (calc_dist(cluster[m][i], pontos[j][0], cluster[m+1][i], pontos[j][1])**2)
        m += 2
    sse.append(valor)

print "fim"