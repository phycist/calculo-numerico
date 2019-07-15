#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################       
'''
neste modulo vamos desenvolver um método para realizar
derifação númerica
'''
##########################
#   bibliotecas 
##########################
from  math import *
from auxilio.decoradores import * 

##########################
# parametros
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = []
h = []
fxh = []
diferenca = []
derivada = []
tabela = []
################################
#  métodos
def contruir_tabela_teste():
    global a,b,c,d # para list não precisa 
    for i in range(3):
        for j in range(3):
            if i == j:
               for k in range(3):
                   if i == k:
                      print(a[i],b[j],c[k])
                      d.append([a[i],b[i],c[i]])


'-----------------------------------------------------'
###########################################
# métodos com decoradores

##########################################

def chamar_fx(funcao,x):
    return funcao(x)
'----------------------------------------------'    
def chamar_fx_h_diferenca(funcao,x,h):
    return funcao(x,h)
'------------------------------------------------'
def contruir_tabela_calculo_derivada_no_terminal(nhs,funcao,ponto,h_tamanho,variacao_funcao):
    print("--------------------------------------")    
    print("    tabela derivada númerica       \
           \n--------------------------------------\
    \n h     | f(x+h)  | f(x+h) - f(x) | df(x)/dx  \
     \n------------------------------------------------")
    for i in range(nhs): #h
        h.append(h_tamanho/(i+1))
        for j in range(nhs): # h | f(x+h)
            if i == j:
               x = ponto + h[j]
               fxh.append(chamar_fx(funcao,x))        
               for k in range(nhs): # h | f(x+h) | f(x+h)-f(x)
                   if i == k:
                      diferenca.append(chamar_fx_h_diferenca(variacao_funcao,x,h[k]))
                      for l in range(nhs): #h | f(x+h) | f(x+h)-f(x)|  df/dx
                          if i == l:   
                             derivada.append((diferenca[l]/h[i]))
                             tabela.append([h[i],'|',fxh[j],'|',diferenca[k],'|',derivada[l]]) #chamem em multiplos de 2
                             print("%.4f |%.4f   | %.4f       | %.4f"  %(h[i],fxh[j],diferenca[k],derivada[l]))
                             
'----------------------------------------------------------------------------------------------------------------'
def contruir_tabela_calculo_derivada(nhs,funcao,ponto,h_tamanho,variacao_funcao):
    for i in range(nhs): #h
        h.append(h_tamanho/(i+1))
        for j in range(nhs): # h | f(x+h)
            if i == j:
               x = ponto + h[j]
               fxh.append(chamar_fx(funcao,x))        
               for k in range(nhs): # h | f(x+h) | f(x+h)-f(x)
                   if i == k:
                      diferenca.append(chamar_fx_h_diferenca(variacao_funcao,x,h[k]))
                      for l in range(nhs): #h | f(x+h) | f(x+h)-f(x)|  df/dx
                          if i == l:   
                             derivada.append((diferenca[l]/h[i]))
                             tabela.append([h[i],'|',fxh[j],'|',diferenca[k],'|',derivada[l]]) #chamem em multiplos de 2
 
'----------------------------------------------------------------------------------------------------------------'




###########################################
'---------------- testes-------------------'
###########################################
'-----  métodos para contrução da derivada ----'
# primeiro termo núnero de pontos
# segundo é funcao para um certo valor
# terceiro é a largura entre os pontos
# quarto é funcão para o calculo da derivada
# contruir_tabela_calculo_derivada(5,cos,30,0.2,diferenca_cos)
# contruir_tabela_calculo_derivada_no_terminal(5,cos,30,0.2,diferenca_cos)
#############################################################
'-----------chamar métodos---------------'
#contruir_tabela_teste()   
#contruir_tabela_calculo_derivada(5,cos,30,0.2,diferenca_cos)



