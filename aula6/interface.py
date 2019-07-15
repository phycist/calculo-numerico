#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################       
'''
neste modulo vamos desenvolve
a inteface grafica
'''
##########################
#   bibliotecas 
##########################
from tkinter import *
from sys import exit
################################

'Gerar a tela principal'
principal = Tk()

'colocando titulo'
principal.title("Cálculo Numerico")

# inserir o menu bar na janela
menubar = Menu(principal)
principal.config(menu=menubar)

#criar as opçoes do menu
' arquivo '
arquivo = Menu(menubar)
menubar.add_cascade(label="Arquivo", menu=arquivo)
arquivo.add_command(label="Sair", command= exit)

'ajuda'
ajuda = Menu(menubar)
menubar.add_command(label="Ajuda")



'mostrar na tela'
principal.mainloop()
