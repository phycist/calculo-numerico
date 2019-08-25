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
#######################3
class Janela:
    def __init__(self,toplevel):
        'criar o frame'
        self.frame=Frame(toplevel)
        self.frame.pack()
        
        'colocar um texto'
        self.texto=Label(self.frame, text='clique para ficar amarelo')
        self.texto['width']=26
        self.texto['height']=3
        self.texto.pack()

        'colocar botão'
        self.botaoverde=Button(self.frame,text='clique')
        self.botaoverde['background']='green'
        self.botaoverde.bind("<Button-1>",self.muda_cor)
        self.botaoverde.pack()

    def muda_cor(self, event):
        # muda a cor do botao
        if self.botaoverde['bg']=='green':
           self.botaoverde['bg']='yellow'
           self.texto['text']='Clique para ficar verde'
        else:
           self.botaoverde['bg']='green'
           self.texto['text']='clique para ficor amarelo'

raiz =Tk()
Janela(raiz)
raiz.mainloop()

