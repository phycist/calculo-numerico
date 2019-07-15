#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################
'''
vamos criar uma biblioteca para o nosso script
derivação-numerica.py 
Nesse script vamos ter funçoes 
polinomio, cos, sen, exp, log, tag, funcões exponencias
'''
#########################
#  Bibliotecas  #
########################
from math import *
########################
'decorador'
# decorador-diferença
def decoradores_diferenca(func):
    def decorador_diferenca(x,h):
        #print(func(x,h)-func(x,0))
        return func(x,h)-func(x,0)
    return decorador_diferenca

########################
@decoradores_diferencas
def diferenca_cos(x,h):
    return cos(x+h)

@decoradores_diferencas
def diferenca_sen(x,h):
    return sin(x+h)

@decorador_diferencas
def diferenca_tang(x,h):
    return tan(x+h)

@decorator_diferencas
def diferenca_exp(x,h):
    return exp(x+h)

@decorator_diferencas
def diferenca_log(x,h):
    return log(x+h)


