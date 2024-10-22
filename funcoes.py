from tkinter import *
import interface as itf

def btn_numeros(numero):
    pega_numero = itf.campo_numeros.get()
    itf.campo_numeros.delete(0,END)
    itf.campo_numeros.insert(0, str(pega_numero) + str(numero))
    return

def limpa_campo():
    itf.campo_numeros.delete(0,END)
    return

def subtracao():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'subtracao'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def multiplicacao():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'multiplicacao'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def divisao():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'divisao'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def soma():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'soma'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def raiz():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'raiz'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def potencia():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'potencia'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def porcentagem():
    pega_numero = itf.campo_numeros.get()
    global primeiro_numero
    global operacao
    operacao = 'porcentagem'
    primeiro_numero = float(pega_numero)
    itf.campo_numeros.delete(0, END)
    return

def igual():
    pega_numero = itf.campo_numeros.get()
    itf.campo_numeros.delete(0, END)
    if operacao == 'soma':
        itf.campo_numeros.insert(0, primeiro_numero + float(pega_numero))

    elif operacao == 'subtracao':
        itf.campo_numeros.insert(0, primeiro_numero - float(pega_numero))

    elif operacao == 'multiplicacao':
        itf.campo_numeros.insert(0, primeiro_numero * float(pega_numero))

    elif operacao == 'divisao':
        itf.campo_numeros.insert(0, primeiro_numero / float(pega_numero))

    elif operacao == 'porcentagem':
        itf.campo_numeros.insert(0, (primeiro_numero * float(pega_numero))/100)

    elif operacao == 'potencia':
        itf.campo_numeros.insert(0, primeiro_numero ** float(pega_numero))

    elif operacao == 'raiz':
        itf.campo_numeros.insert(0, primeiro_numero ** (1/2))
    return