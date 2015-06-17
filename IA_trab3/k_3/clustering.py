from numpy import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calc_dist(a, b, c, d):
    dist = math.sqrt(((a-b)**2)+((c-d)**2))
    return dist

np.random.seed(1)
arquivo = pd.read_csv("artificial_3.data", header=None, sep=',')
valores = arquivo.iloc[:,:2]

matrix = valores.as_matrix()
x=[]
y=[]
for px, py in matrix:
    x.append(px)
    y.append(py)
    
#forma o grafico dos dados antes da classificacao
plt.clf()
plt.scatter(x, y, alpha=0.5, c='green')
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Antes de classificar')
plt.savefig('antes.png')

#cria os pontos de cluster
pontos = []
np.random.seed(1)
for i in range(3):
    pX = np.random.normal(np.mean(x), np.std(x), 1)
    pY = np.random.normal(np.mean(y), np.std(y), 1)    
    pontos.append([pX, pY])

#controla as iteracoes
cluster = dict()
for itera in range(1, 10):
    cluster.clear()
    for px, py in matrix:
        distancia = []
        for i in range(len(pontos)):
            distancia.append(calc_dist(px, pontos[i][0], py, pontos[i][1]))
    #print distancia
    cluster[(px,py)] = distancia.index(min(distancia))
    
'''       
    titulo = "Iteracao {} com {} pontos".format(itera, 2)
    saver = "depois_{}.png".format(itera)
    plt.clf()
    plt.scatter(x1, y1, alpha=0.5, c='r')
    plt.scatter(x2, y2, alpha=0.5, c='b')
    plt.scatter(pX, pY, s=100, c='r', alpha=0.2)
    plt.scatter(pX1, pY1, s=100, c='b', alpha=0.2)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title(titulo)
    plt.savefig(saver)
    
    somaPx = 0
    somaPy = 0
    for px, py in ponto_1:
        somaPx += px
        somaPy += py
    if len(ponto_1)>0:
        pX = somaPx/len(ponto_1)
        pY = somaPy/len(ponto_1)
    
    somaPx = 0
    somaPy = 0
    for px, py in ponto_2:
        somaPx += px
        somaPy += py
    if len(ponto_2)>0:
        pX1 = somaPx/len(ponto_2)
        pY1 = somaPy/len(ponto_2)
'''
print "fim"