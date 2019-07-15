import os,sys
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
from sys import exit
from auxilio.derivacao_numerica import *
################################
'#################################################################################'
#                            'criando telas'
'################################################################################'
'###########TELA GRAFICO#################'
class Derivar :
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        #inserir o menu bar na janela
        self.menubar = Menu(master)
        self.menuarquivo = Menu(self.menubar)
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
        self.opcoes.add_command(label="Estatística")
        self.opcoes.add_command(label="Derivada númerica")
        self.opcoes.add_command(label="Integral númerica")
        self.opcoes.add_command(label="Resolução de sistemas lineares")
        self.opcoes.add_command(label="A proximação de funções")
        self.opcoes.add_command(label="Determinação de polinomios")
        self.opcoes.add_command(label="Polinomios de interpolação")
        'ajuda'
        self.ajuda = Menu(self.menubar)
        self.menubar.add_command(label="Ajuda")
        #final--- menu         
        master.config(menu=self.menubar)      
      # conteudo
       # quero colocar isso aqui num conteiner
        self.containermaior=Frame(master)
        self.container1=Frame(self.containermaior)
        self.L1 = Label(self.container1, text="")
        self.L1.pack()
        self.L2 = Label(self.container1, text="")
        self.L2.pack()
        self.container2=Frame(self.containermaior)
        self.container1.grid(row=0,column=0)
        # criando uma tabela
        self.container2.grid(row=1, column=0)
        'mostrar na tela'
        self.containermaior.pack(side=LEFT)
 
        # médtodos do quadro 
        def Derivar_funcao():
            '''
            Vamos obter a derivada de função qualquer
            '''
            contruir_tabela_calculo_derivada(5,cos,30,0.2,diferenca_cos)
            texto=str(tabela[-1][-1])
            # mostrar valor 
            self.L1["text"]="O valor da derivada"
            self.L2["text"]=texto 
               


        # Mostrar as funionalidades
        botao=Button(self.containermaior, text="Derivar",command=Derivar_funcao)
        botao.grid(row=2,column=0)


