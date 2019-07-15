#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################
'''
neste metódo vamos desenvolver um método para realizar
derifação númerica
'''
##########################
#   bibliotecas 
##########################
from  math import *
##########################
# parametros
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = []
################################
#  métodos
def contruir_tabela():
    global a,b,c,d # para list não precisa 
    for i in range(3):
        for j in range(3):
            if i == j:
               for k in range(3):
                   if i == k:
                      print(a[i],b[j],c[k])
                      d.append([a[i],b[i],c[i]])

###########################################
# métodos com decoradores

#############################################################
#chamar métodos
#contruir_tabela()   
