from numpy import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calc_dist(a, b, c, d):
    dist = math.sqrt(((a-b)**2)+((c-d)**2))
    return dist

np.random.seed(1)
arquivo = pd.read_csv("artificial_2.data", header=None, sep=',')
valores = arquivo.iloc[:,:2]

matrix = valores.as_matrix()
x=[]
y=[]
for px, py in matrix:
    x.append(px)
    y.append(py)
    

plt.clf()
plt.scatter(x, y, alpha=0.5, c='green')
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Antes de classificar')
plt.savefig('antes.png')

pontos = []
np.random.seed(1)
for i in range(2):
    pX = np.random.sample()+1
    pY = np.random.sample()+1
    pontos.append([pX, pY])
    
pX = pontos[0][0]
pY = pontos[0][1]
pX1 = pontos[1][0]
pY1 = pontos[1][1]

for itera in range(1, 10):
    distancia = []
    ponto_1 = []
    ponto_2 = []
    for px, py in matrix:
        distancia.append([calc_dist(px, pX, py, pY), calc_dist(px, pX1, py, pY1)])
        if distancia[-1][0] < distancia[-1][1]:
            ponto_1.append([px, py])
        else:
            ponto_2.append([px, py])
    
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for a, b in ponto_1:
        x1.append(a)
        y1.append(b)
    for a, b in ponto_2:
        x2.append(a)
        y2.append(b)
    
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

print "fim"