#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
########################
'''
teste para importacao
'''
from  auxilio.importacao_test2 import para_importacao

print("buscanco a variavel b na classe para importacao")
print(para_importacao.b)

from auxilio.importacao_test2 import a
print("buscando a variavel a  fora desta classe")
print(a)
