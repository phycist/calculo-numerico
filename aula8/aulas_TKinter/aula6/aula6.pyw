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
#######################
class Janela:
    def __init__(self,toplevel):
        '1 tela'
        self.frame = Frame(toplevel)
        self.frame.pack()
    
        '2 tela'
        self.frame2=Frame(toplevel)
        self.frame2.pack()

        'titulo'
        self.titulo =Label(self.frame,text='Vidente 2005',font=('Verdana','13','bold'))
        self.titulo.pack()
        
        'mensagem'
        self.msg=Label(self.frame,width=40,height=6,text = 'Adivinho o evento ocorrido!')
        self.msg.focus_force()
        self.msg.pack()

        'Definindo botão 1'
        self.b01=Button(self.frame2,text='Botão 1')
        self.b01['padx'],self.b01['pady'] = 10, 5
        self.b01['bg']='deepskyblue'
        self.b01.bind("<Return>",self.keypress01)
        self.b01.bind("<Any-Button>",self.button01)
        self.b01.bind("<FocusIn>",self.fin01)
        self.b01.bind("<FocusOut>",self.fout01)
        self.b01['relief']=RIDGE
        self.b01.pack(side=LEFT)
        
        'Definindo botao 2'
        self.b02=Button(self.frame2,text='Botão 2')
        self.b02['padx'],self.b02['pady'] = 10, 5
        self.b02['bg']='deepskyblue'
        self.b02.bind("<Return>",self.keypress02)
        self.b02.bind("<Any-Button>",self.button02)
        self.b02.bind("<FocusIn>",self.fin02)
        self.b02.bind("<FocusOut>",self.fout02)
        self.b02['relief']=RIDGE
        self.b02.pack(side=LEFT)


    def keypress01(self,event):
        self.msg['text']='ENTER sobre o Botão 1'
    def keypress02(self,event):
        self.msg['text']='ENTER sobre o Botão 2'
    def button01(self,event):
        self.msg['text']='Clique sobre o Botão 1'
    def button02(self,event):
        self.msg['text']='Clique sobre o Botão 2'
    def fin01(self,event):
        self.b01['relief']=FLAT
    def fout01(self,event):
        self.b01['relief']=RIDGE
    def fin02(self,event): 
        self.b02['relief']=FLAT
    def fout02(self,event): 
        self.b02['relief']=RIDGE


raiz=Tk()
Janela(raiz)
raiz.mainloop()







