import string
import random
import time
from tkinter.constants import N, S
from typing import Sized
import PySimpleGUI as sg
from os import system
from PySimpleGUI.PySimpleGUI import R, Input

#limpa a tela
def clear():
    system('cls')

#Gera a senha
def gerar(L, m, M, n, e, a):
    clear()
    c = int(L)
    senha = []
    Lista = []
    if m:
        Lista.append(min())
        c-=1
    if M:
        Lista.append(mai())
        c-=1
    if n:
        Lista.append(num())
        c-=1
    if e:
        Lista.append(esp())
        c-=1
    if a:
        Lista.append(ace())
        c-=1
    senha.extend(Lista)
    for i in range(c):
        Lista = []
        if m:
            Lista.append(min())
        if M:
            Lista.append(mai())
        if n:
            Lista.append(num())
        if e:
            Lista.append(esp())
        if a:
            Lista.append(ace())
        New = random.choice(Lista)
        senha.append(New)        
    random.shuffle(senha)
    senha = "".join(senha)
    
    return senha  
    
#Sorteia um caractere minusculo
def min():
    v = random.choice(string.ascii_lowercase)
    return v

#Sorteia um caractere maiusculo
def mai():
    v = random.choice(string.ascii_uppercase)
    return v

#Sorteia um numero
def num():
    v = random.choice(string.digits)
    return v

#Sorteia um caractere especial
def esp():
    v = random.choice(['3','!','$','%','&','*','?','@','_'])
    return v

#Sorteia um acento
def ace():
    v = random.choice(['^','`','~','´','^'])
    return v


class Screen():
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Comprimento da senha:')],
            [sg.Slider(range=(0,20),default_value=8,orientation='h', size=(23,20), key='Len')],
            [sg.Text('Caracteres:')],
            [sg.Checkbox('Maiúsculas', key='Mai', size=(9,0),default=True),sg.Checkbox('Minúsculas', key='Min',default=True)],
            [sg.Checkbox('Números', key='Num', size=(9,0),default=True),sg.Checkbox('Especiais', key='Esp',default=True)],
            [sg.Checkbox('Acentos', key='Ace', size=(9,2),default=False)],
            [sg.Button('GERAR SENHA')]#,
            #[sg.Output(size=(28,3))]
        ]
        #Janela
        self.janela = sg.Window('Gerador de senha').layout(layout)
    def Iniciar(self):
        while True:
            #Extrair dados da tela            
            self.button, self.values = self.janela.read()
            
            if self.values!=None:
                clear()
                Len = self.values['Len']
                Mai = self.values['Mai']
                Min = self.values['Min']
                Num = self.values['Num']
                Esp = self.values['Esp']
                Ace = self.values['Ace']

                _L = 0
                if Min:
                    _L +=1
                if Mai:
                    _L +=1
                if Num:
                    _L +=1
                if Esp:
                    _L +=1
                if Ace:
                    _L +=1
                if Len>=_L:
                    senha = gerar(Len, Min, Mai, Num, Esp, Ace)
                    print('A senha gerada foi:')
                    print(senha)
                else:
                    print("O comprimento não é suficiente  para cumprir os requesitos")
            else:
                exit()

tela = Screen()
tela.Iniciar()