#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################       
'''
neste modulo vamos desenvolver a inteface grafica 
para nosso programa de calculo númerico.
'''
##########################
#   bibliotecas 
##########################
from tkinter import *
from integrar_funcao import Integrar
from derivar_funcao import  Derivar
from levantargrafico import Grafico
from sys import exit
from auxilio.polinomios_interpolacao import *
###########################
'##################criando a tela Princial#############################'
class Principal:
      def __init__(self, master):
         self.frame = Frame(master)
         self.frame.pack()
         #inserir o menu bar na janela
         self.menubar = Menu(master)
         self.menuarquivo = Menu(self.menubar)
             # metodos
         def chamar_grafico():
             root = Tk()
             'Definir o tamanho tela'
             Grafico(root)             
         def chamar_integrar():
             root = Tk()
             Integrar(root)
         def chamar_Derivar():
             root = Tk()
             'Definir o tamanho tela'
             root.geometry('400x300')
             Derivar(root)             
         



        #criando as opçoes do menu
         'arquivo'
         self.menubar.add_cascade(label="Arquivo", menu=self.menuarquivo)
         self.menuarquivo.add_command(label="Novo")
         self.menuarquivo.add_command(label="Sair", command= exit)
         
         'editar'
         self.editar = Menu(self.menubar)
         self.menubar.add_cascade(label="Editar", menu=self.editar)
         'opções'
         self.opcoes = Menu(self.menubar)
         self.menubar.add_cascade(label="calcular", menu=self.opcoes)
         self.opcoes.add_command(label="Construir gráfico de função", command=chamar_grafico)
         self.opcoes.add_command(label="Derivada númerica",command=chamar_Derivar)
         self.opcoes.add_command(label="Integral númerica", command=chamar_integrar)
         'ajuda'
         self.ajuda = Menu(self.menubar)
         self.menubar.add_command(label="Ajuda")

        #final         
         master.config(menu=self.menubar)         

raiz = Tk()
'Definir o tamanho da tela'
raiz.geometry('400x300')
'O Titulo do calculo númerico'
raiz.title("Cálculo Numerico")
Principal(raiz)
raiz.mainloop()

#######################################################################################
