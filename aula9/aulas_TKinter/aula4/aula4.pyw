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



class Packing:
    def __init__(self,instancia_Tk):
       
        self.container1=Frame(instancia_Tk)
        self.container1.pack()
        Button(self.container1,text='B1').pack()
        
        
        self.container2=Frame(instancia_Tk)
        Button(self.container2,text='B2').pack(side=LEFT)
        Button(self.container2,text='B3').pack(side=LEFT)
        self.container2.pack()


        self.container3=Frame(instancia_Tk)
        self.b4=Button(self.container3,text='B4')
        self.b5=Button(self.container3,text='B5')
        self.b6=Button(self.container3,text='B6')
        self.b6.pack(side=RIGHT)
        self.b4.pack(side=RIGHT)
        self.b5.pack(side=RIGHT)
        self.container3.pack()
        
        
        
       
        #self.b6.pack(side=RIGHT)
        #self.b4.pack(side=RIGHT)
       # self.b5.pack(side=RIGHT)


raiz=Tk()
Packing(raiz)
raiz.mainloop()
