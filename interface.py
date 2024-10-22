from tkinter import *
import funcoes as fc

calculadora = Tk()
calculadora.title('Canculadora - Jb')
calculadora.geometry('480x475+500+100')
calculadora.resizable(width=False, height=False)
calculadora.config(bg = '#002a3b')

campo_numeros = Entry(calculadora, width = 50)
campo_numeros.place(x = 90, y= 25)

btn1 = Button(calculadora, text= '1', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(1))
btn1.place(x = 50, y = 150)

btn2 = Button(calculadora, text= '2', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(2))
btn2.place(x = 150, y = 150)

btn3 = Button(calculadora, text= '3', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(3))
btn3.place(x = 250, y = 150)

btn4 = Button(calculadora, text= '4', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(4))
btn4.place(x = 50, y = 225)

btn5 = Button(calculadora, text= '5', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(5))
btn5.place(x = 150, y = 225)

btn6 = Button(calculadora, text= '6', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(6))
btn6.place(x = 250, y = 225)

btn7 = Button(calculadora, text= '7', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(7))
btn7.place(x = 50, y = 300)

btn8 = Button(calculadora, text= '8', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(8))
btn8.place(x = 150, y = 300)

btn9 = Button(calculadora, text= '9', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(9))
btn9.place(x = 250, y = 300)

btn0 = Button(calculadora, text= '0', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros(0))
btn0.place(x = 150, y = 375)

btn_virgula = Button(calculadora, text= '.', relief=FLAT, width=10, height=3, command=lambda:fc.btn_numeros('.'))
btn_virgula.place(x = 50, y = 375)

btn_igual = Button(calculadora, text= '=', relief=FLAT, width=10, height=3, command=fc.igual)
btn_igual.place(x = 250, y = 375)

btn_divisao = Button(calculadora, text= '/', relief=FLAT, width=10, height=3, command=fc.divisao)
btn_divisao.place(x = 350, y = 150)

btn_multiplicacao = Button(calculadora, text= '*', relief=FLAT, width=10, height=3, command=fc.multiplicacao)
btn_multiplicacao.place(x = 350, y = 225)

btn_soma = Button(calculadora, text= '+', relief=FLAT, width=10, height=3, command=fc.soma)
btn_soma.place(x = 350, y = 300)

btn_subtracao = Button(calculadora, text= '-', relief=FLAT, width=10, height=3, command=fc.subtracao)
btn_subtracao.place(x = 350, y = 375)

btn_limpa = Button(calculadora, text= 'C', relief=FLAT, width=10, height=3, command=fc.limpa_campo)
btn_limpa.place(x = 50, y = 75)

btn_porcentagem = Button(calculadora, text= '%', relief=FLAT, width=10, height=3, command=fc.porcentagem)
btn_porcentagem.place(x = 150, y = 75)

btn_potencia = Button(calculadora, text= 'xⁿ', relief=FLAT, width=10, height=3, command=fc.potencia)
btn_potencia.place(x = 250, y = 75)

btn_raiz = Button(calculadora, text= '√', relief=FLAT, width=10, height=3, command=fc.raiz)
btn_raiz.place(x = 350, y = 75)

feitoPor=Label(calculadora, text = 'Desenvolvido por Jarbas Tesch')
feitoPor.place(x=150, y=455)

calculadora.mainloop()