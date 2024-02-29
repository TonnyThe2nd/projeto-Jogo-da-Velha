
from tkinter import *
from tkinter import messagebox

# cor de fundo -> #636363
# azul escuro - > #636396
# vermelho - > #DB0F08
# azul claro - > #00997D
# cinza claro - > #A9A9A9
c = '#A9A9A9'
v = '#DB0F08'
a = '#00997D'
x = 0
y = 0
contador = 0
verificador = ''
class Jogo_Velha:
    def encerrar(self):
        if x > y:
            messagebox.showinfo('Fim de jogo!', f'Jogador 2 ganhou com {x} pontos!.')
        elif y > x:
            messagebox.showinfo('Fim de jogo!', f'Jogador 1 ganhou com {y} pontos!.')
        else:
            messagebox.showinfo('Fim de jogo!', 'EMPATE!')
        win.destroy()
    def reiniciar(self):
        global contador
        self.b_0['text'] = ''
        self.b_1['text'] = ''
        self.b_2['text'] = ''
        self.b_3['text'] = ''
        self.b_4['text'] = ''
        self.b_5['text'] = ''
        self.b_6['text'] = ''
        self.b_7['text'] = ''
        self.b_8['text'] = ''
        contador = 0
    def inicio_jogo(self, frame_jogo):
        botao_start = Button(text='Sair', command=self.encerrar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
        botao_start.place(x=50,y=130)
        botao_reinicio = Button(text='Reiniciar', command=self.reiniciar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
        botao_reinicio.place(x=160,y=130)
        vertical = Label(frame_jogo, text='', height=25, relief='flat',pady=10, font=('Aryal 5 bold'), bg='#FFF')
        vertical.place(x=102, y=30)
        vertical = Label(frame_jogo, text='', height=25, relief='flat',pady=10, font=('Aryal 5 bold'), bg='#FFF')
        vertical.place(x=182, y=30)

        horizontal = Label(frame_jogo, text='', width=106, relief='flat',padx=10, font=('Aryal 2 bold'), bg='#FFF')
        horizontal.place(x=20, y=90)
        horizontal = Label(frame_jogo, text='', width=106, relief='flat',padx=10, font=('Aryal 2 bold'), bg='#FFF')
        horizontal.place(x=20, y=160)

        self.b_0 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but0)
        self.b_0.place(x=27,y = 30)
        self.b_1 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but1)
        self.b_1.place(x=108,y = 30)
        self.b_2 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but2)
        self.b_2.place(x=192,y = 30)

        self.b_3 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but3)
        self.b_3.place(x=27,y = 100)
        self.b_4 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but4)
        self.b_4.place(x=108,y = 100)
        self.b_5 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but5)
        self.b_5.place(x=192,y = 100)

        self.b_6 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but6)
        self.b_6.place(x=27,y = 170)
        self.b_7 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but7)
        self.b_7.place(x=108,y = 170)
        self.b_8 = Button(frame_jogo, text='', width=4, height=1,font=('Aryal',21), bg='#636363', overrelief=RIDGE, relief='flat', command=self.but8)
        self.b_8.place(x=192,y = 170)
    def jogo(self):
        global verificador
        global contador
        while contador<=9:
            contador+=1
            return contador
    def contar(self):
        global x
        global y
        global contador
        valor = self.jogo()
        if valor % 2 != 0:
            text = 'X'
        else:
            text = 'O'
        match text:
            case 'O':
                val = int(o_jogador_ponto['text'])
                x = val + 1
                o_jogador_ponto.config(text=str(x)) 
                contador = 0
            case 'X':
                val = int(x_jogador_ponto['text'])
                y = val + 1
                x_jogador_ponto.config(text=str(y))
                contador = 0
        self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
        self.next.place(x=110, y=370)
    def limpar(self):
        global y
        global x
        global contador
        self.b_0['text'] = ''
        self.b_1['text'] = ''
        self.b_2['text'] = ''
        self.b_3['text'] = ''
        self.b_4['text'] = ''
        self.b_5['text'] = ''
        self.b_6['text'] = ''
        self.b_7['text'] = ''
        self.b_8['text'] = ''
        contador=0
        self.next.destroy()
        

    def but0(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_0.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_0.config(text=texto, fg = a)
        if self.b_0['text'] == self.b_1['text'] and self.b_1['text'] == self.b_2['text'] and self.b_0['text'] == self.b_2['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 8
        elif self.b_0['text'] == self.b_4['text'] and self.b_0['text'] == self.b_8['text'] and self.b_4['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 8
        elif self.b_0['text'] == self.b_3['text'] and self.b_0['text'] == self.b_6['text'] and self.b_6['text'] == self.b_3['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else: 
            if contador == 9: 
                contador = 10
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
    def but1(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_1.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_1.config(text=texto, fg = a)
        if self.b_0['text'] == self.b_1['text'] and self.b_1['text'] == self.b_2['text'] and self.b_0['text'] == self.b_2['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_1['text'] == self.b_4['text'] and self.b_1['text'] == self.b_7['text'] and self.b_7['text'] == self.b_4['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:  
                contador = 10
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
            
    def but2(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_2.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_2.config(text=texto, fg = a)
        if self.b_0['text'] == self.b_1['text'] and self.b_1['text'] == self.b_2['text'] and self.b_0['text'] == self.b_2['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_2['text'] == self.b_4['text'] and self.b_2['text'] == self.b_6['text'] and self.b_4['text'] == self.b_6['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_2['text'] == self.b_5['text'] and self.b_2['text'] == self.b_5['text'] and self.b_5['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:  
                contador = 10
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
        
    def but3(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_3.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_3.config(text=texto, fg = a)
        if self.b_3['text'] == self.b_4['text'] and self.b_3['text'] == self.b_5['text'] and self.b_4['text'] == self.b_5['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_0['text'] == self.b_3['text'] and self.b_0['text'] == self.b_6['text'] and self.b_6['text'] == self.b_3['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:
                contador = 10  
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
            
    def but4(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_4.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_4.config(text=texto, fg = a)
        if self.b_3['text'] == self.b_4['text'] and self.b_3['text'] == self.b_5['text'] and self.b_4['text'] == self.b_5['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_0['text'] == self.b_4['text'] and self.b_0['text'] == self.b_8['text'] and self.b_4['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_2['text'] == self.b_4['text'] and self.b_2['text'] == self.b_6['text'] and self.b_4['text'] == self.b_6['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_1['text'] == self.b_4['text'] and self.b_1['text'] == self.b_7['text'] and self.b_7['text'] == self.b_4['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:  
                contador = 10
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
            
    def but5(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_5.config(text=texto, fg=v)
        else:
            texto = 'O', 
            self.b_5.config(text=texto, fg=a)
        if self.b_3['text'] == self.b_4['text'] and self.b_3['text'] == self.b_5['text'] and self.b_4['text'] == self.b_5['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_2['text'] == self.b_5['text'] and self.b_2['text'] == self.b_8['text'] and self.b_5['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:
                contador = 10  
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
    def but6(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_6.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_6.config(text=texto, fg=a)
        if self.b_6['text'] == self.b_7['text'] and self.b_6['text'] == self.b_8['text'] and self.b_7['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_2['text'] == self.b_4['text'] and self.b_2['text'] == self.b_6['text'] and self.b_4['text'] == self.b_6['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_0['text'] == self.b_3['text'] and self.b_0['text'] == self.b_6['text'] and self.b_6['text'] == self.b_3['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9: 
                contador = 10 
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)

    def but7(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_7.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_7.config(text=texto, fg=a)
        if self.b_6['text'] == self.b_7['text'] and self.b_6['text'] == self.b_8['text'] and self.b_7['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_1['text'] == self.b_4['text'] and self.b_1['text'] == self.b_7['text'] and self.b_7['text'] == self.b_4['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:  
                contador = 10
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
    def but8(self):
        global contador
        global verificador
        valor = self.jogo()
        if valor % 2 == 0:
            texto = 'X'
            self.b_8.config(text=texto, fg=v)
        else:
            texto = 'O'
            self.b_8.config(text=texto, fg=a)
        if self.b_6['text'] == self.b_7['text'] and self.b_6['text'] == self.b_8['text'] and self.b_7['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_0['text'] == self.b_4['text'] and self.b_0['text'] == self.b_8['text'] and self.b_4['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        elif self.b_2['text'] == self.b_5['text'] and self.b_2['text'] == self.b_5['text'] and self.b_5['text'] == self.b_8['text']:
            verificador = 'Vencedor'
            self.contar()
            contador = 10
        else:
            if contador == 9:  
                contador = 10
                self.next =  Button(text='Próximo', command=self.limpar, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
                self.next.place(x=109, y=370)
    def frame(self):
        frame_jogo = Frame(win, bg='#636363', width=280, height=250, relief='raised')
        frame_jogo.grid(row=1, column=0, padx=10, pady=10, sticky=NW)
        self.inicio_jogo(frame_jogo)
    def but_inicio(self):
        botao_start = Button(text='Iniciar', command=self.frame, width=10, font=('Aryal 10 bold'), relief=RAISED, overrelief=RIDGE)
        botao_start.place(x=110,y=130)
        

win = Tk()
win.geometry('300x400')
win.maxsize(300,400)
win.configure(bg='#636363')

frame_tabela = Frame(win, bg='#636396', width=280, height=100, relief='raised')
frame_tabela.grid(row=0, column=0, padx=10, pady=10, sticky=NW)

frame_jogo = Frame(win, bg='#636363', width=280, height=240, relief='raised')
frame_jogo.grid(row=1, column=0, sticky=NW)

x_jogador = Label(frame_tabela, text='X', font=('Aryal 40 bold'), bg='#636396', fg='#DB0F08')
x_jogador.place(x=30, y=10)
x_jogador = Label(frame_tabela, text='Jogador 1', font=('Aryal 10 bold'), bg='#636396', fg='#FFF')
x_jogador.place(x=15, y=70)
x_jogador_ponto = Label(frame_tabela, text='0', font=('Aryal 30 bold'),bg='#636396', fg='#FFF')
x_jogador_ponto.place(x=90, y=20)

ponto = Label(frame_tabela, text=':',font=('Aryal 30 bold'),bg='#636396', fg='#FFF')
ponto.place(x=135, y=20)

o_jogador = Label(frame_tabela, text='O', font=('Aryal 40 bold'), bg='#636396', fg='#00997D')
o_jogador.place(x=210, y=10)
o_jogador = Label(frame_tabela, text='Jogador 2', font=('Aryal 10 bold'), bg='#636396', fg='#FFF')
o_jogador.place(x=200, y=70)
o_jogador_ponto = Label(frame_tabela, text='0', font=('Aryal 30 bold'),bg='#636396', fg='#FFF')
o_jogador_ponto.place(x=170, y=20)
jogo_velha = Jogo_Velha()
jogo_velha.but_inicio()
win.mainloop()