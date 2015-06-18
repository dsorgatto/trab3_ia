from numpy import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# funcao para calculo da distancia euclidiana
def calc_dist(a, b, c, d):
    dist = math.sqrt(((a-b)**2)+((c-d)**2))
    return dist

#funcao que gera os cluster
def clusteriza(seed_val, x, y, k, grafico):
    #cria os pontos do cluster
    pontos = []
    np.random.seed(seed_val)
    for i in range(k):
        pX = list(np.random.normal(np.mean(x), np.std(x), 1))
        pY = list(np.random.normal(np.mean(y), np.std(y), 1))   
        pontos.append([pX, pY])
    
    #controla as iteracoes
    itera = 0
    comparador = True
    while itera <= 50 and comparador:
        itera += 1
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
        
        #gera os graficos para o SEED_VALUE pedido
        if grafico:
            #gera o grafico dos clusters
            titulo = "Iteracao {} com {} pontos".format(itera, k)
            saver = "depois_{}.png".format(itera)
            cores = ['b', 'r', 'y', 'g', 'c', 'm', 'k', 'w', '0.5', '0.25']
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
        contador = 0
        for i in range(k):
            if len(cluster[i*2])> 0:
                a = pontos[i][0]
                pontos[i][0] = np.mean(cluster[j])
                if a == pontos[i][0]:
                    contador += 1
                j += 1
                a = pontos[i][1]
                pontos[i][1] = np.mean(cluster[j])
                if a == pontos[i][1]:
                    contador += 1
                j += 1
        
        #verifica se houve convergencia
        if contador == k*2:
            comparador = False
            
    #calculo da Soma do Erro Quadratico
    valor = 0.0
    m = 0
    for j in range(k):
        for i in range(len(cluster[m])):
            valor += (calc_dist(cluster[m][i], pontos[j][0], cluster[m+1][i], pontos[j][1])**2)
        m += 2
    return valor


#Valor de K para esse dataset
k = input("Digite o valor de K: ")
nome = "artificial_{}.data".format(k)
#abre o arquivo e o converte em dois vetores X e Y
arquivo = pd.read_csv(nome, header=None, sep=',')
valores = arquivo.iloc[:,:2]
matrix = valores.as_matrix()
x=[]
y=[]
for px, py in matrix:
    x.append(px)
    y.append(py)  

#forma o grafico dos dados antes da classificacao
titulo = "Antes de classificar \n K={}".format(k)
saver = "antes_k{}.png".format(k)
plt.clf()
plt.scatter(x, y, alpha=0.5, c='green')
plt.ylabel('Y')
plt.xlabel('X')
plt.title(titulo)
plt.savefig(saver)

sse = []
seed_val = []
grafico = False
for z in range(10):
    seed_val.append(z*2)
    valor = clusteriza(z*2, x, y, k, grafico)
    sse.append(valor)

#grafico da evolucao do SSE
titulo = "Evolucao da soma do erro quadratico\n K={}".format(k)
saver = "erro_k{}.png".format(k)
plt.clf()
plt.plot(seed_val, sse, c='r')
plt.title(titulo)
plt.ylabel('SSE')
plt.xlabel('SEED_VALUES')
plt.savefig(saver)
print "fim da clusterizacao"

escolha = raw_input("Deseja gerar os graficos de classificacao? [S,N] ")
if escolha.lower()=='s':
    escolha = input("Digite o SEED_VALUE que deseja plotar: ")
    grafico = True
    clusteriza(escolha, x, y, k, grafico)
    print "Fim da plotagem"
else:
    print "Fim do processamento"