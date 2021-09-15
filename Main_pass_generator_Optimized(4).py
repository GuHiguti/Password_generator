import string
import random
import time
from os import system
from typing import AsyncContextManager, Match

#limpa a tela
def clear():
    system('cls')

#Gera a senha
def gerar(c, m, M, n, e, a):
    clear()
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

def sete():
    global _T, comprimento, minusculas, maiusculas, numeros, especiais, acentos, tempo_inicio
    tempo_aqui = time.time()
    _g = ""
    senha = gerar(comprimento, minusculas, maiusculas, numeros, especiais, acentos)
    if senha==None and tempo_aqui-tempo_inicio<3:
        sete()
    else:
        if tempo_aqui-tempo_inicio>=3:
            print("\n\tO tempo de processamento ultrapassou o limite permitido")
            print(_T)
        else:
            print("\n\tA senha gerada é:",senha)
        _g = input("\n\n\tDeseja sortear de novo? s/n\n\t")
        if _g=="s" or _g=="sim":
            tempo_inicio = time.time()
            sete()

comprimento = 8
minusculas = True
maiusculas = True
numeros = True
especiais = True
acentos = False

#main loop
while True:
    clear()
    len = 0
    #Escreve na tela as possibilidades de ação
    print(f'''
        0 - Fechar programa

        1 - Determinar comprimento da senha
            Atual: {comprimento}

        2 - Letras minúsculas: {minusculas}

        3 - Letras maiúsculas: {maiusculas}

        4 - Números: {numeros}

        5 - Caracteres especiais: {especiais}

        6 - Acentos: {acentos}

        7 - GERAR

        
        Inserir ação: ''', end="")

    action = input()

    if action=='0':
        clear()
        exit()
    elif action=='1':
        clear()
        comprimento = int(input("\n\tDigite o novo comprimento da senha: "))
    elif action=='2':
        if minusculas:
            minusculas=False
        elif not minusculas:
            minusculas=True
    elif action=='3':
        if maiusculas:
            maiusculas=False
        elif not maiusculas:
            maiusculas=True
    elif action=='4':
        if numeros:
            numeros=False
        elif not numeros:
            numeros=True
    elif action=='5':
        if especiais:
            especiais=False
        elif not especiais:
            especiais=True
    elif action=="6":
        if acentos:
            acentos=False
        elif not acentos:
            acentos=True
    elif action=='7':
        if minusculas:
            len +=1
        if maiusculas:
            len +=1
        if numeros:
            len +=1
        if especiais:
            len +=1
        if acentos:
            len +=1
        if comprimento>=len:
            _T = 0
            tempo_inicio = time.time()
            sete()
        else:
            print("\n\tO comprimento não é suficiente para cumprir os requesitos")
            input()
    else:
        clear()
        print("\n\tA ação solicitada é inválida")
        time.sleep(1.5)