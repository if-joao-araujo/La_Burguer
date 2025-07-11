##---------------importações--------------------##
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


##---------Interface da janela --------------------##
janela_menu = Tk()
janela_menu.title("La_burguer_menu")
janela_menu.geometry("1300x1000")

##---------------imagem do la burguer -----------##
papel_parede = Image.open("/home/joao-pedro/Documents/GitHub/La_Burguer/imagens/La-burguer (2).png")
tk_imagem = ImageTk.PhotoImage(papel_parede)
label_da_imagem = Label(janela_menu, image=tk_imagem)
label_da_imagem.pack()

##---------------Contadores do carrinho --------------##
def atualizar_contadores(item):
    label_do_contador[item].config(text=str(contador_itens[item]))

def adiciona_do_contador(item):
    contador_itens[item] += 1
    atualizar_contadores(item)

def decrementa_do_carrinho(item):
    if contador_itens [item] >0:
       contador_itens [item] -=1
       atualizar_contadores(item)

##----------------contadores que serão exibidos--------------##
contador_itens = {
          'item1':0,
          'item2':0,
          'item3':0,
          'item4':0}

label_do_contador = {'item1':Label(janela_menu, text="0"),
                     'item2':Label(janela_menu, text="0"),
                     'item3':Label(janela_menu, text="0"),
                     'item4':Label(janela_menu, text="0")}

label_do_contador['item1'].place(x=200,y=600)
label_do_contador['item2'].place(x=480,y=600)
label_do_contador['item3'].place(x=730,y=600)
label_do_contador['item4'].place(x=1000,y=600)


##-------  Botões do carrinho   ----------------##
botao1 = Button(janela_menu,
                text='Adicionar ao carrinho',
                fg='blue',
                command=lambda:adiciona_do_contador('item1'))
botao1.place(x=200,y=550, width=135,height=35)

botao2 = Button(janela_menu,
                text='Adicionar ao carrinho',
                fg='blue',
                 command=lambda:adiciona_do_contador('item2'))
botao2.place(x=480,y=550,width=135,height=35)

botao3 = Button(janela_menu,
                text='Adicionar ao carrinho',
                fg='blue',
                 command=lambda:adiciona_do_contador('item3'))
botao3.place( x=730,y=550,width=135,height=35)

botao4 = Button(janela_menu,
               text='Adicionar ao carrinho',
                fg='blue',
                command=lambda:adiciona_do_contador('item4'))
botao4.place(x=1000,y=550,width=135,height=35)

##------------Botão para remover itens -------------------##
botao1_remover = Button(janela_menu,
                text='X',
                fg='red',
                bd=8,
                relief='groove',
                command=lambda:decrementa_do_carrinho('item1'))
botao1_remover.place(x=250,y=585, width=80,height=30)

botao2_remover = Button(janela_menu,
                text='X',
                fg='red',
                bd=8,
                relief='groove',
                  command=lambda:decrementa_do_carrinho('item2'))
botao2_remover.place(x=520,y=585, width=80,height=30)

botao3_remover = Button(janela_menu,
                text='X',
                fg='red',
                bd=8,
                relief='groove',
                  command=lambda:decrementa_do_carrinho('item3'))
botao3_remover.place( x=780,y=585, width=80,height=30)

botao4_remover = Button(janela_menu,
               text='X',
                fg='red',
                bd=8,
                relief='groove',
                command=lambda:decrementa_do_carrinho('item4'))
botao4_remover.place(x=1050,y=585, width=80,height=30) 

##-------------------botão para prosseguir ---------------------------------------------##
def prosseguir_compra():
    total = sum(contador_itens.values())
    if total == 0:
        messagebox.showwarning("Carrinho vazio", "Adicione itens ao carrinho antes de prosseguir.")
    else:
        finalizar_compra()

botao_prosseguir = Button(janela_menu,
                          text="Prosseguir com a compra",
                          fg="white",
                          bg="green",
                          font=("Arial", 12, "bold"),
                          command=prosseguir_compra)
botao_prosseguir.place(x=550, y=630, width=200, height=40)

##-----------------janela finalizar compra------------------------------------##
def finalizar_compra():
    janela_finaalizar = Toplevel()
    janela_finaalizar.title("Finalizar compra")
    janela_finaalizar.geometry("500x500")

    #-----mostrando os itens ------------#
    frame_itens = Frame(janela_finaalizar)
    frame_itens.pack(pady=20)

    titulo = Label(frame_itens,text="Itens selecionados")
    titulo.pack()
     
    ##-------cardapio para exibir o valor da compra------------## 
    cardapio = {"Classico da casa":24,
                "Egg burguer":25,
                "Smash Tradicional":27,
                "Cheese e bacon":28}
     
    ##---------------- valor total da compra -------------------------##
    valor_total = 0

    ##--------------------somando o preço dos lanches --------------##
    valor_lanche = 0
    contador = 1
    for chave,valor in cardapio.items():
        valor_lanche = valor*contador_itens[f'item{contador}']
        cardapio[chave] = valor_lanche
        valor_total += valor_lanche
        contador+=1
 
  ##--------------------exibindo os lanches selecionados --------------##
    for item, quantidade in cardapio.items():
        Label(frame_itens,text=f"{item} : {quantidade}R$",
                  font="Aerial 12").pack()
    preco_a_pagar = Label(frame_itens,text=f"valor total: {valor_total}R$" ,font="Aerial 12")
    preco_a_pagar.pack()   

    janela_finaalizar.mainloop()

janela_menu.mainloop()
