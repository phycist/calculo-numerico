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
from auxilio.polinomios_interpolacao import *
################################
'#################################################################################'
#                            'criando telas'
'################################################################################'
'###########TELA GRAFICO#################'
class Grafico :
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
         self.L1 = Label(self.container1, text="X  Y")
         self.L1.pack()
         self.container2=Frame(self.containermaior)
         self.container1.grid(row=0,column=0)
        # criando uma tabela
         self.container2.grid(row=1, column=0)
         valor =''
         'valores de x'
         x1=Entry(self.container2, textvariable = valor, background="white",width=10)
         x1.grid(row =2 , column = 0)
         x2=Entry(self.container2, textvariable = valor, background="white",width=10)
         x2.grid(row =3 , column = 0)
         x3=Entry(self.container2, textvariable = valor, background="white",width=10)
         x3.grid(row =4 , column = 0)
         x4=Entry(self.container2, textvariable = valor, background="white",width=10)
         x4.grid(row =5 , column = 0)
         x5=Entry(self.container2, textvariable = valor, background="white",width=10)
         x5.grid(row =6 , column = 0)
         x6=Entry(self.container2, textvariable = valor, background="white",width=10)
         x6.grid(row =7 , column = 0)
         x7=Entry(self.container2, textvariable = valor, background="white",width=10)
         x7.grid(row =8 , column = 0)
         x8=Entry(self.container2, textvariable = valor, background="white",width=10)
         x8.grid(row =9 , column = 0)
         x9=Entry(self.container2, textvariable = valor, background="white",width=10)
         x9.grid(row =10 , column = 0)
         x10=Entry(self.container2, textvariable = valor, background="white",width=10)
         x10.grid(row =11 , column = 0)
         'valores de y'
         y1=Entry(self.container2, textvariable = valor, background="white",width=10)
         y1.grid(row =2 , column = 1)
         y2=Entry(self.container2, textvariable = valor, background="white",width=10)
         y2.grid(row =3 , column = 1)
         y3=Entry(self.container2, textvariable = valor, background="white",width=10)
         y3.grid(row =4 , column = 1)
         y4=Entry(self.container2, textvariable = valor, background="white",width=10)
         y4.grid(row =5 , column = 1)
         y5=Entry(self.container2, textvariable = valor, background="white",width=10)
         y5.grid(row =6 , column = 1)
         y6=Entry(self.container2, textvariable = valor, background="white",width=10)
         y6.grid(row =7 , column = 1)
         y7=Entry(self.container2, textvariable = valor, background="white",width=10)
         y7.grid(row =8 , column = 1)
         y8=Entry(self.container2, textvariable = valor, background="white",width=10)
         y8.grid(row =9 , column = 1)
         y9=Entry(self.container2, textvariable = valor, background="white",width=10)
         y9.grid(row =10 , column = 1)
         y10=Entry(self.container2, textvariable = valor, background="white",width=10)
         y10.grid(row =11 , column = 1)
         'mostrar na tela'
         self.containermaior.pack(side=LEFT)
        # médtodos do quadro 
         def contruir_grafico():
             self.x = [x1.get(),x2.get(),x3.get(),x4.get(),x5.get(),x6.get(),x7.get(),x8.get(),x9.get(),x10.get()]
             self.y = [y1.get(),y2.get(),y3.get(),y4.get(),y5.get(),y6.get(),y7.get(),y8.get(),y9.get(),y10.get()]
             x = []
             y = []
             for i in range(len(self.x)):
                 if self.x[i]!='':
                    x.append(float(self.x[i]))
             for j in range(len(self.y)):
                 if self.y[j]!='':
                    y.append(float(self.y[j]))
              
             #contruir grafico
            # plotar_polinomio_interpolacao(dados_xtest,dados_ytest,'Titulo',[0,10],'abscisa',[0,100],'ordenada', 'ro',1000)
             plotar_polinomio_interpolacao(x,y,'Titulo',[0,len(x)+5],'titulo_x',[0,len(y)+5],'titulo_y','ro',1000)

               


         # Mostrar as funionalidades
         botao=Button(self.containermaior, text="plotar",command=contruir_grafico)
         botao.grid(row=11,column=1)

###0#########################################################################################################
