from distutils.cmd import Command
from hashlib import new
from sqlite3 import Cursor
from tkinter import *
from tkinter import messagebox
from random import randint
import mysql.connector

# cores-----------------
co0 = '#f0f3f5' #preto
co1 = '#feffff' #branco
co2 = '#3fb5a3' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra

conexao = mysql.connector.connect(host='localhost',user='root',password='',database='voldrek20')

Cursor = conexao.cursor


def destruir():
    for widget in frame_baixo.winfo_children():
            widget.destroy()
            
    for widget in frame_cima.winfo_children():
            widget.destroy()

login = Tk()
login.geometry('310x300')
login.resizable(width=False , height=False)
login.configure(background=co1)

#Dividindo tela
frame_cima = Frame(login,width=310 , height=50, bg=co1 , relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(login,width=310 , height=250, bg=co1 , relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando frame_cima
l_nome = Label(frame_cima, text='LOGIN' , anchor=NE , font=('Ivy 25') ,bg=co1 , fg=co4)
l_nome.place(x=5 , y=5)
l_linha = Label(frame_cima, text='' ,width=275, anchor=NW , font=('Ivy 1') ,bg=co2 , fg=co4)
l_linha.place(x=10 , y=45)

credenciais = ['lucas','123','admin','admin','','']


def verifica_senha():

    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo admin')

    elif credenciais [0] == nome and credenciais[1] == senha:
    
        messagebox.showinfo('Login', 'Seja bem vindo de volta '+credenciais[0])

        destruir()
        
        nova_janela()
        
    else:
        messagebox.showwarning('Erro', 'verifique a senha')

def tela_cadastro():

    destruir()

    def cadastrar_bd_mysql():
            #comando = 
            Cursor.execute (f'''INSERT INTO login ('nome','senha','email') VALUES ('{e_c_nome}','{e_c_senha}','{e_c_email}')''')

            
    #frame cima
    l_nome = Label(frame_cima, text='Cadastro' , anchor=NE , font=('Ivy 25') ,bg=co1 , fg=co4)
    l_nome.place(x=5 , y=5)
    l_linha = Label(frame_cima, text='' ,width=275, anchor=NW , font=('Ivy 1') ,bg=co2 , fg=co4)
    l_linha.place(x=10 , y=45)

    #frame baixo
    l_c_nome = Label(frame_baixo, text='Nome *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_c_nome.place(x=10 , y=20)
    e_c_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
    e_c_nome.place (x=14, y=50)

    l_c_senha = Label(frame_baixo, text='senha *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_c_senha.place(x=10 , y=80)
    e_c_senha = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
    e_c_senha.place (x=14, y=110)

    l_c_email = Label(frame_baixo, text='Email *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
    l_c_email.place(x=10 , y=140)
    e_c_email = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
    e_c_email.place (x=14, y=160)

    b_confirmar = Button(frame_baixo, command=cadastrar_bd_mysql , text='Confirmar' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
    b_confirmar.place(x=150 , y=210)

    

def nova_janela():

    def D20():
        d20 = randint(1 , 20)
        resultado['text'] = d20
    def D12():
        d12 = randint(1 , 12)
        resultado['text'] = d12
    def D10():
        d10 = randint(1 , 10)
        resultado['text'] = d10
    def D8():
        d8 = randint(1 , 8)
        resultado['text'] = d8
    def D6():
        d6 = randint(1 , 6)
        resultado['text'] = d6
    def D4():
        d4 = randint(1 , 4)
        resultado['text'] = d4

    l_nome = Label(frame_cima, text='Usuário: '+credenciais[0] , anchor=NE , font=('Ivy 20') ,bg=co1 , fg=co4)
    l_nome.place(x=5 , y=5)

    l_linha = Label(frame_cima, text='' ,width=275, anchor=NW , font=('Ivy 1') ,bg=co2 , fg=co4)
    l_linha.place(x=10 , y=45)

    b_D20 = Button(frame_baixo, command=D20, text='D20' ,width=5 ,height=2 , font=('Ivy 8') ,bg=co2 , fg=co0, relief=RAISED, overrelief=RIDGE)
    b_D20.place(x=260, y=195)

    b_D12 = Button(frame_baixo, command=D12, text='D12' ,width=5 ,height=2 , font=('Ivy 8') ,bg=co2 , fg=co0, relief=RAISED, overrelief=RIDGE)
    b_D12.place(x=260 , y=150)

    b_D10 = Button(frame_baixo, command=D10, text='D10' ,width=5 ,height=2 , font=('Ivy 8') ,bg=co2 , fg=co0, relief=RAISED, overrelief=RIDGE)
    b_D10.place(x=260 , y=105)

    b_D8 = Button(frame_baixo, command=D8, text='D8' ,width=5 ,height=2 , font=('Ivy 8') ,bg=co2 , fg=co0, relief=RAISED, overrelief=RIDGE)
    b_D8.place(x=5 , y=105)

    b_D6 = Button(frame_baixo, command=D6, text='D6' ,width=5 ,height=2 , font=('Ivy 8') ,bg=co2 , fg=co0, relief=RAISED, overrelief=RIDGE)
    b_D6.place(x=5 , y=150)

    b_D4 = Button(frame_baixo, command=D4, text='D4' ,width=5 ,height=2 , font=('Ivy 8') ,bg=co2 , fg=co0, relief=RAISED, overrelief=RIDGE)
    b_D4.place(x=5, y=195)

    resultado = Label(frame_baixo, text='' ,anchor=NW , font=('Ivy 25 bold') ,bg=co1 , fg=co4)
    resultado.place(x=130 , y=130)
    m_resultado = Label(frame_baixo, text='RESULTADO' ,anchor=NW , font=('Ivy 15 bold') ,bg=co1 , fg=co4)
    m_resultado.place(x=90 , y=100)

#configurando frame baixo
l_nome = Label(frame_baixo, text='Nome *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
l_nome.place(x=10 , y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
e_nome.place (x=14, y=50)

#senha
l_pass = Label(frame_baixo, text='Senha *' , anchor=NW , font=('Ivy 10') ,bg=co1 , fg=co4)
l_pass.place(x=10 , y=95)
e_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=('', 15), highlightthickness=1, relief='solid')
e_pass.place (x=14, y=130)

b_confirmar = Button(frame_baixo, command=verifica_senha, text='Entrar' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15 , y=180)

b_cadastro = Button(frame_baixo, command=tela_cadastro, text='Cadastro' ,width=10,height=2, anchor=NW , font=('Ivy 8 bold') ,bg=co2 , fg=co1, relief=RAISED, overrelief=RIDGE)
b_cadastro.place(x=200 , y=180)

login.mainloop()
Cursor.close()
conexao.close()