#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################
'''
Nesse script temos como o objetivo 
calcular os polinômios para interpolaçâo
'''
##################################
#     Bibliotecas                #
###################################
from scipy.interpolate import lagrange
import matplotlib.pyplot as plotar
####################################
#   variaveis para teste
###################################
dados_xtest=[1,2,3,4]
dados_ytest=[12,32,21,45]
######################################
#        Métodos                     #
#####################################
' Entrada de dados Dados '
def entrar_dados():
    sair="n"
    x,y = [],[]
    while sair=="n" or sair=='N':
          xi=input("Passe um valor para x :")
          yi=input("Passe um valor para y :")
          x_i=float(xi)
          y_i=float(yi)
          x.append(x_i)
          y.append(y_i)
          sair = input("Você gostaria de sair(s) ou Não(n)")    
    print("------ \n  tabela \
           \n------\
    \n x | y \
     \n------")
    for i in range(len(x)):
        print( x[i],'|',y[i])
    return [x,y]
' colocando os pontos '
def colocar_pontos(dados_x, dados_y):
    plotar.plot(dados_x, dados_y,'ro')

' levatamento do polinomio de lagrange'
def levantar_polinomio_lagrange(dados_x, dados_y):
    polinomio = lagrange(dados_x, dados_y)
    return polinomio 

' levatando a curva'
def levantar_curva(polinomio,pontos):
    print(polinomio)
    x = list(range(pontos))
    x
    y = []
    for i in range(pontos):
#        print(polinomio(x[i]))   
        y.append(polinomio(x[i]))   
#    print(y)
    return [x,y] 

' criar o grafico '
def criar_grafico_polinomio(npontos, dados_x,dados_y):
    polinomio = levantar_polinomio_lagrange(dados_x, dados_y)
    
    pontos = levantar_curva(polinomio,npontos)
    plotar.plot(pontos[0],pontos[1],'b-')
 
def ajustar_grafico(titulo,nome_eixox,nome_eixoy,lista_escala_x, lista_escala_y, dados_x,dados_y):
    'acertando a escala'
    plotar.xlim(lista_escala_x[0],lista_escala_x[-1])
    plotar.ylim(lista_escala_y[0],lista_escala_y[-1])
    'titulo'
    plotar.title(titulo)
    'nome dos eixos'
    plotar.xlabel(nome_eixox)
    plotar.ylabel(nome_eixoy)
    "acrescentar a equação"
    polinomio = levantar_polinomio_lagrange(dados_x, dados_y)
    plotar.text(int((lista_escala_x[-1]-lista_escala_x[0])/2),int((lista_escala_y[-1]-lista_escala_y[0])/2)+2,"Equação do gráfico")
    plotar.text(int((lista_escala_x[-1]-lista_escala_x[0])/2),int((lista_escala_y[-1]-lista_escala_y[0])/2),str(polinomio))



def plotar_polinomio_interpolacao(dados_x,dados_y,Titulo,x_tamanho,titulo_x,y_tamanho,titulo_y, macardor,interacao):
    plotar.plot(dados_x, dados_y, macardor) # macador = 'ro'
    criar_grafico_polinomio(interacao,dados_x, dados_y) # interacao >= 1000
    ajustar_grafico(Titulo,titulo_x,titulo_y,x_tamanho,y_tamanho,dados_x,dados_y)
    plotar.show() 

#############################################################
#               chamar os metodos teste 
###############################################################
' entrada de dados'
#entrar_dados()
'levatar o polinomio de lagrange'
#polinomio = levantar_polinomio_lagrange(dados_xtest, dados_ytest)
#print(polinomio)
#plotar.plot(dados_xtest, dados_ytest,'ro')
#plotar.show()

' levatar a curva'
#criar_grafico_polinomio(1000,dados_xtest,dados_ytest)
#plotar.show()
'ajustar grafico'
#ajustar_grafico('Meu Título','abiscissa','ordenada',[0,10],[0,100],dados_xtest,dados_ytest)
#plotar.show()
#colocar a curva
#plotar_polinomio_interpolacao(dados_xtest,dados_ytest,'Titulo',[0,10],'abscisa',[0,100],'ordenada', 'ro',1000)
'tera aequação do grafico'






