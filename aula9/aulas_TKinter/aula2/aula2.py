#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
#########################       
'Aulas Tkinter'
'''
Para não aparecer a janela do script salve pyw

'''
##########################
#   bibliotecas 
##########################
from tkinter import *

'criando uma janela adequandamente'
class Janela:
    def __init__(self,toplevel):
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
        self.botao = Button(self.frame1, text='oi', background="green")
        self.botao.pack()


raiz=Tk()
Janela(raiz)
raiz.mainloop()

