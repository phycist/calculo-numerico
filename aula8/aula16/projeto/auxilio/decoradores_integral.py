#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################
'''
vamos criar uma biblioteca para o nosso script
integração-numerica.py 
Nesse script vamos ter funçoes 
polinomio, cos, sen, exp, log, tag.

'''
#########################
#  Bibliotecas  #
########################
from math import *
########################

'##############################decoradores################################################################'
#decorador gerar imagem
def decorador_gerar_imagens(func):
    def decorador_gerar_imagens_interior(x):
        y = []
        for i in range(len(x)):
            imagem = func(x[i])
            y.append(imagem)
       #print("A imagem")
        #print(y)
        return y
    return decorador_gerar_imagens_interior

'##############################################################################3'
# decorador realizar integral
def decorador_regra_trapezio(func):
    def decorador_regra_trapezio_interior(x,h):
        trapezio = []
        y = []
        #print("a imagens y ")
        for i in range(len(x)):
            y.append(func(x[i],0))
        #print(y)
        for i in range(len(y)):
            if  i < len(y)-1:
                trapezio.append((y[i]+y[i+1])*(h/2))
        #print("A integral")
       # print(trapezio)
        #print(sum(trapezio))
        return sum(trapezio)
    return decorador_regra_trapezio_interior


def decorador_regra_um_terco_simpsom(func):
    def decorador_regra_um_terco(x,h):
        simpson = []
        y = []
        #print("a imagens y")
        for i in range(len(x)):
            y.append(func(x[i],0))
        # print(y)
        for i in range(len(x)):
            if  i < len(x)-2:
                simpson.append((y[i]+4*y[i+1]+y[i+2])*(h/3))
      #  print("A integral")
      #  print(simpson)
      #  print(sum(simpson))
        return sum(simpson)
    return decorador_regra_um_terco


def decorador_regra_tres__oitavos_simpsom(func):
    def decorador_regra_tres_oitavos(x,h):
        simpson = []
        y = []
        #print("a imagens y")
        for i in range(len(x)):
            y.append(func(x[i],0))
        # print(y)
        for i in range(len(x)):
            if  i < len(x)-3:
                simpson.append((y[i]+4*(y[i+1]+y[i+2])+y[i+3])*(h/3))
      #  print("A integral")
      #  print(simpson)
      #  print(sum(simpson))
        return sum(simpson)
    return decorador_regra_tres_oitavos


def decorador_regra_dois__quinze_simpsom(func):
    def decorador_regra_dois_quinze(x,h):
        simpson = []
        y = []
        #print("a imagens y")
        for i in range(len(x)):
            y.append(func(x[i],0))
        # print(y)
        for i in range(len(x)):
            if  i < len(x)-4:
                simpson.append(((2/15*h)*(7*y[i] +((32/3)*(y[i+1]+y[i+3])+4*(y[i+2])+7*y[i+4]))))
      #  print("A integral")
      #  print(simpson)
      #  print(sum(simpson))
        return sum(simpson)
    return decorador_regra_dois_quinze


def decorador_regra_dois__quinze_simpsonav(func):
    def decorador_regra_dois_quinzeav(x,h):
        simpson = []
        y = []
        #print("a imagens y")
        for i in range(len(x)):
            y.append(func(x[i],0))
        # print(y)
        for i in range(len(x)):
            if  i < len(x)-5:
                simpson.append()
      #  print("A integral")
      #  print(simpson)
      #  print(sum(simpson))
        return sum(simpson)
    return decorador_regra_dois_quinzeav
'##############################################################################################################'
'##############################################################################################################'
###################################################################################################################
################################# funções decoradas#######################################################
'----------------------Gerar imagens ------------------------------------'
@decorador_gerar_imagens
def imagens_cos(x):
    return cos(x)

@decorador_gerar_imagens
def imagens_sen(x):
    return sen(x)

@decorador_gerar_imagens
def imagens_tang(x):
    return tan(x)

@decorador_gerar_imagens
def imagens_log(x):
    return log(x)

@decorador_gerar_imagens
def imagens_exp(x):
    return exp(x)


# ter as imagens
#imagens_cos([25,30,45])
#input()
'---------------------------------------ok-------------------------------------------------------------------'
'''
decorador_regra_trapezio,decorador_regra_um_terco_simpsom,decorador_regra_tres__oitavos_simpson,
decorador_regra_dois__quinze_simpson,  decorador_regra_dois__quinze_simpsonav
'''
'    regra do trapezio    '
@decorador_regra_trapezio
def integral_trapezio_cos(x,h):
    return cos(x)

@decorador_regra_trapezio
def integral_trapezio_sen(x,h):
    return sen(x)

@decorador_regra_trapezio
def integral_trapezio_tan(x,h):
    return tan(x)

@decorador_regra_trapezio
def integral_trapezio_exp(x,h):
    return exp(x)

@decorador_regra_trapezio
def integral_trapezio_log(x,h):
    return log(x)

'***************************************************************'
'decorador_regra_um_terco_simpson'
@decorador_regra_um_terco_simpsom
def integral_regra_um_terco_simpson_cos(x,h):
    return cos(x)

@decorador_regra_um_terco_simpsom
def integral_regra_um_terco_simpson_sen(x,h):
    return sen(x)


@decorador_regra_um_terco_simpsom
def integral_regra_um_terco_simpson_tan(x,h):
    return tan(x)

@decorador_regra_um_terco_simpsom
def integral_regra_um_terco_simpson_exp(x,h):
    return exp(x)

@decorador_regra_um_terco_simpsom
def integral_regra_um_terco_simpson_log(x,h):
    return log(x)
'*****************************************************************'
' decorador_regra_tres_oitavos'

@decorador_regra_tres__oitavos_simpsom
def integral_regra_tres_oitavos_simpson_cos(x,h):
    return cos(x)

@decorador_regra_tres__oitavos_simpsom
def integral_regra_tres_oitavos_simpson_sen(x,h):
    return sen(x)

@decorador_regra_tres__oitavos_simpsom
def integral_regra_tres_oitavos_simpson_tan(x,h):
    return tan(x)


@decorador_regra_tres__oitavos_simpsom
def integral_regra_tres_oitavos_simpson_exp(x,h):
    return exp(x)


@decorador_regra_tres__oitavos_simpsom
def integral_regra_tres_oitavos_simpson_log(x,h):
    return log(x)
'''
'*****************************************************************************'
'decorador_regra_dois__quinze_simpson,'
'''
@decorador_regra_dois__quinze_simpsom
def integral_regra_dois_quinze_simpson_cos(x,h):
    return cos(x)

@decorador_regra_dois__quinze_simpsom
def integral_regra_dois_quinze_simpson_sen(x,h):
    return sen(x)

@decorador_regra_dois__quinze_simpsom
def integral_regra_dois_quinze_simpson_tan(x,h):
    return tan(x)

@decorador_regra_dois__quinze_simpsom
def integral_regra_dois_quinze_simpson_exp(x,h):
    return exp(x)

@decorador_regra_dois__quinze_simpsom
def integral_regra_dois_quinze_simpson_log(x,h):
    return log(x)
'  decorador_regra_dois__quinze_simpsonav'
@decorador_regra_dois__quinze_simpsonav
def integral_regra_dois_quinze_simpsonav_cos(x,h):
    return cos(x)

@decorador_regra_dois__quinze_simpsonav
def integral_regra_dois_quinze_simpsonav_sen(x,h):
    return sen(x)

@decorador_regra_dois__quinze_simpsonav
def integral_regra_dois_quinze_simpsonav_tan(x,h):
    return tan(x)

@decorador_regra_dois__quinze_simpsonav
def integral_regra_dois_quinze_simpsonav_exp(x,h):
    return exp(x)

@decorador_regra_dois__quinze_simpsonav
def integral_regra_dois_quinze_simpsonav_log(x,h):
    return log(x)


############################## testes ######################################################################

#print(" teste integral imagem")
#integral_cos([25,30,35],5)
#print("ok")
#input()
