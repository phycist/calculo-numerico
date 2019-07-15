#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################
'''
criar exemplo decoradores de função

'''
#decorador simples

'ideia básica'
def funcao1(a,b):
    print(a+b)
soma = funcao1
soma(1,2)
###############################################
# 'decorador de funcao'
def funcao_decoradora(funcao):
    def funcao_interior():
        print("vamos realizar um calculo")
        funcao()
        print("fim do calculo")
    return funcao_interior

@funcao_decoradora
def soma():
    print(10 + 20)

soma()
#########################################################
import math
# 'funcao decoradora com parametros ilimitados'
def funcao_decoradora_parametros(funcao_parametro):
    def funcao_interior(*args):       
        print("vamos realizar um calculo:")
        funcao_parametro(*args)
        print("terminando o calculo")
    return funcao_interior
@funcao_decoradora_parametros
def somas(num1, num2, num3):
    print(num1+num2+num3)
somas(1,2,3)
#########################################################
def decorador(func):
    def interior(a,b):
        print(func(a,b)-func(a,0))
    return interior
@decorador
def cosseno(x,h):
    return cos(x+h)

cosseno(45,0.2)
####################################################################
def decorador_rad_grau(func):
    def rad_grau(x):
        x = func((pi/180)*x)
        return x
    return rad_grau
##############################################################
'decoradores alinhados'
def primeiro_decorador(func):
    def interior():
        print("primeiro decorador")
        return func()
    return interior

def segundo_decorador(func):
    def interior():
        print("segundo decorador")
        return func()
    return interior

@primeiro_decorador
@segundo_decorador
def oi():
    print("aqui")
####################################################################




















