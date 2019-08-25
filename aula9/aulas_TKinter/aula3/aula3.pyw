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

class Janela:
    def __init__(self,toplevel):
        'criar a janela'
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        'colocando um botão'
        self.botao1 = Button(self.frame1, text='oi')
        self.botao1['background']='green'
        self.botao1['font']=('Verdana','12','italic','bold')
        self.botao1['height']=3
        self.botao1.pack()
        
        self.botao2 = Button(self.frame1, bg='white', text='bola', font=('Times',16))    
        self.botao2.pack()                                         



raiz=Tk()
Janela(raiz)
raiz.mainloop()

