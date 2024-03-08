from tkinter import *
from tkinter import messagebox
from random import randint

#Sorteia quem começa o jogo, jogador 1 ou jogador 2
jogador = randint(1,2)


# RESETA AS VARIÁVEIS ------------------------------------------
b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = 0
rodada = 0
pontuacao_j1 = 0
pontuacao_j2 = 0

#---------------------------------------------------
#FUNÇÃO PARA SER EXECUTADA EM CADA CLIQUE -------
def clique(n_botao):
   
    #chama variável global
    global jogador, b1, b2, b3, b4, b5, b6, b7, b8, b9, rodada, pontuacao_j1, pontuacao_j2


    rodada += 1


    if jogador == 1:
        simbolo = "X"
        cor = "blue"
    else:
        simbolo = "O"
        cor = "red"


    if n_botao == 1:
        botao1.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b1 = jogador
    elif n_botao == 2:
        botao2.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b2 = jogador
    elif n_botao == 3:
        botao3.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b3 = jogador
    elif n_botao == 4:
        botao4.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b4 = jogador
    elif n_botao == 5:
        botao5.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b5 = jogador
    elif n_botao == 6:
        botao6.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b6 = jogador      
    elif n_botao == 7:
        botao7.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b7 = jogador
    elif n_botao == 8:
        botao8.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b8 = jogador
    elif n_botao == 9:
        botao9.config(text=simbolo, state=DISABLED, relief=SUNKEN, bg=cor)
        b9 = jogador


    if (b1 == 1 and b2 == 1 and b3 == 1) or (b4 == 1 and b5 == 1 and b6 == 1) or (b7 == 1 and b8 == 1 and b9 == 1) or (b1 == 1 and b4 == 1 and b7 == 1) or (b2 == 1 and b5 == 1 and b8 == 1) or (b3 == 1 and b6 == 1 and b9 == 1) or (b1 == 1 and b5 == 1 and b9 == 1) or (b3 == 1 and b5 == 1 and b7 == 1):
        messagebox.showinfo("TEMOS UM VENCEDOR", "O JOGADOR 1 (X) VENCEU!")
        pontuacao_j1 += 1
        pontos_j1["text"] = pontuacao_j1
        reset()


    elif (b1 == 2 and b2 == 2 and b3 == 2) or (b4 == 2 and b5 == 2 and b6 == 2) or (b7 == 2 and b8 == 2 and b9 == 2) or (b1 == 2 and b4 == 2 and b7 == 2) or (b2 == 2 and b5 == 2 and b8 == 2) or (b3 == 2 and b6 == 2 and b9 == 2) or (b1 == 2 and b5 == 2 and b9 == 2) or (b3 == 2 and b5 == 2 and b7 == 2):
        messagebox.showinfo("TEMOS UM VENCEDOR", "O JOGADOR 2 (O) VENCEU!")
        pontuacao_j2 += 1
        pontos_j2["text"] = pontuacao_j2
        reset()
    elif rodada == 9:
        messagebox.showinfo("VELHA!", "DEU EMPATE!")
        reset()


    #muda a vez do jogador da próxima rodada
    if jogador == 1:
        jogador = 2
        texto_vez["text"] = "É a vez do JOGADOR 2 (O)"
        texto_vez["bg"] = "red"
    else:
        jogador = 1
        texto_vez["text"] = "É a vez do JOGADOR 1 (X)"
        texto_vez["bg"] = "blue"


#---------------------------------------------------
# FUNÇÃO PARA RESETAR OS BOTÕES APÓS O TÉRMINO DA RODADA
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, rodada
    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = rodada = 0
    botao1.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao2.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao3.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao4.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")  
    botao5.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao6.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao7.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao8.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")
    botao9.config(text="", state="normal", relief=RAISED, bg="#f0f0f0")










#---------------------------------------------        
#PRINCIPAL - CRIANDO A JANELA DO JOGO --------
janela = Tk()
janela.title("TIC-TAC-TOE")
janela.geometry("300x470+500+100")
janela.configure(background="#a4a4a4")
janela.resizable(False, False)

#Titulo do jogo -----------------------------------
titulo = Label(janela, text="TIC-TAC-TOE", font="Arial 24",fg="black",bg="#c4c4c4" )
titulo.place(x=50, y=10)

#Criando os botoes - Linha 1 --------------------
botao1 = Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(1))
botao1.place(x=10, y=60)
botao2= Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(2))
botao2.place(x=105, y=60)
botao3 = Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(3))
botao3.place(x=200, y=60)


#Criando os botoes - Linha 2 -------------------
botao4 = Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(4))
botao4.place(x=10, y=155)
botao5= Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(5))
botao5.place(x=105, y=155)
botao6 = Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(6))
botao6.place(x=200, y=155)


#Criando os botoes - Linha 3 -------------------
botao7 = Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(7))
botao7.place(x=10, y=250)
botao8= Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(8))
botao8.place(x=105, y=250)
botao9 = Button(janela,text="",font="Arial 20", width=5, height=2, bg="#f0f0f0", command=lambda: clique(9))
botao9.place(x=200, y=250)


#Texto sobre de quem é a vez da jogada ------------
texto_vez = Label(janela, text="", font="Arial 12",fg="black")
texto_vez.place(x=40, y=350)


#Texto PLACAR -------------------------------------
placar = Label(janela, text="PLACAR", font="Arial 12", fg="black",bg="#a4a4a4" )
placar.place(x=110, y=380) 	


#Texto PLACAR - JOGADOR 1 -----------------------------------
placar_j1 = Label(janela, text="JOGADOR 1 (X):", font="Arial 10", fg="black",bg="#a4a4a4" )
placar_j1.place(x=10, y=400)


#Texto PLACAR - PONTOS DO JOGADOR 1 -----------------------------------
pontos_j1 = Label(janela, text="JOGADOR 1 (X):", font="Arial 12", fg="black",bg="#a4a4a4" )
pontos_j1.place(x=111, y=400)
pontos_j1["text"] = pontuacao_j1


#Texto PLACAR - JOGADOR 2 -----------------------------------
placar_j2 = Label(janela, text="JOGADOR 2 (O):", font="Arial 10", fg="black",bg="#a4a4a4" )
placar_j2.place(x=10, y=420)


#Texto PLACAR - PONTOS DO JOGADOR 2 -----------------------------------
pontos_j2 = Label(janela, text="JOGADOR 1 (X):", font="Arial 12", fg="black",bg="#a4a4a4" )
pontos_j2.place(x=111, y=420)
pontos_j2["text"] = pontuacao_j2


#ALTERA O TEXTO PARA ESCREVER QUEM COMEÇARÁ A PRIMEIRA JOGADA
if jogador == 1:
    texto_vez["text"] = "Você começa JOGADOR 1 (X)"
    texto_vez["bg"] = "blue"
else:
    texto_vez["text"] = "Você começa JOGADOR 2 (O)"
    texto_vez["bg"] = "red"


#Mantém a janela aberta
janela.mainloop()
