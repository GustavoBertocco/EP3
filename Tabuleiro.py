import tkinter as tk
import Jogo
import numpy as np

class Tabuleiro:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("400x500+500+500")  
        self.window.title("Jogo da Velha")
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.rowconfigure(1, minsize=100,weight=1)
        self.window.rowconfigure(2, minsize=100,weight=1)
        self.window.rowconfigure(3, minsize=50,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=100,weight=1)
        self.jogo=Jogo.Jogo()
        
        
        
        self.botao0_0=tk.Button(self.window)
        self.botao0_0.configure(command=self.botao0_0_clicado)
        self.botao0_0.grid(row=0,column=0,sticky='nsew')
        
        self.botao0_1=tk.Button(self.window)
        self.botao0_1.configure(command=self.botao0_1_clicado)
        self.botao0_1.grid(row=0,column=1,sticky='nsew')
        
        self.botao0_2=tk.Button(self.window)
        self.botao0_2.configure(command=self.botao0_2_clicado)
        self.botao0_2.grid(row=0,column=2,sticky='nsew')
        
        self.botao1_0=tk.Button(self.window)
        self.botao1_0.configure(command=self.botao1_0_clicado)
        self.botao1_0.grid(row=1,column=0,sticky='nsew')
        
        self.botao1_1=tk.Button(self.window)
        self.botao1_1.configure(command=self.botao1_1_clicado)
        self.botao1_1.grid(row=1,column=1,sticky='nsew')
        
        self.botao1_2=tk.Button(self.window)
        self.botao1_2.configure(command=self.botao1_2_clicado)
        self.botao1_2.grid(row=1,column=2,sticky='nsew')
        
        self.botao2_0=tk.Button(self.window)
        self.botao2_0.configure(command=self.botao2_0_clicado)
        self.botao2_0.grid(row=2,column=0,sticky='nsew')
        
        self.botao2_1=tk.Button(self.window)
        self.botao2_1.configure(command=self.botao2_1_clicado)
        self.botao2_1.grid(row=2,column=1,sticky='nsew')
        
        self.botao2_2=tk.Button(self.window)
        self.botao2_2.configure(command=self.botao2_2_clicado)
        self.botao2_2.grid(row=2,column=2,sticky='nsew')
        
        self.botao_reiniciar=tk.Button(self.window)
        self.botao_reiniciar.grid(row=4,column=1,sticky='nsew')
        self.botao_reiniciar.configure(text='Reiniciar',command=self.reiniciar,fg='black')
        
        self.label_status=tk.Label()
        self.label_status.configure(text=self.jogo.string_var, font='Arial 20 bold')
        self.label_status.grid(row=3,column=0,columnspan=3)
        
            
    
    
    def reiniciar(self):
        self.jogo.jogadas=1
        self.jogo.a=np.zeros((3,3))
        self.jogo.jogador=1
        self.jogo.string_var='Próxima jogada : X'
        self.botao0_0=tk.Button(self.window)
        self.botao0_0.configure(command=self.botao0_0_clicado)
        self.botao0_0.grid(row=0,column=0,sticky='nsew')
        
        self.botao0_1=tk.Button(self.window)
        self.botao0_1.configure(command=self.botao0_1_clicado)
        self.botao0_1.grid(row=0,column=1,sticky='nsew')
        
        self.botao0_2=tk.Button(self.window)
        self.botao0_2.configure(command=self.botao0_2_clicado)
        self.botao0_2.grid(row=0,column=2,sticky='nsew')
        
        self.botao1_0=tk.Button(self.window)
        self.botao1_0.configure(command=self.botao1_0_clicado)
        self.botao1_0.grid(row=1,column=0,sticky='nsew')
        
        self.botao1_1=tk.Button(self.window)
        self.botao1_1.configure(command=self.botao1_1_clicado)
        self.botao1_1.grid(row=1,column=1,sticky='nsew')
        
        self.botao1_2=tk.Button(self.window)
        self.botao1_2.configure(command=self.botao1_2_clicado)
        self.botao1_2.grid(row=1,column=2,sticky='nsew')
        
        self.botao2_0=tk.Button(self.window)
        self.botao2_0.configure(command=self.botao2_0_clicado)
        self.botao2_0.grid(row=2,column=0,sticky='nsew')
        
        self.botao2_1=tk.Button(self.window)
        self.botao2_1.configure(command=self.botao2_1_clicado)
        self.botao2_1.grid(row=2,column=1,sticky='nsew')
        
        self.botao2_2=tk.Button(self.window)
        self.botao2_2.configure(command=self.botao2_2_clicado)
        self.botao2_2.grid(row=2,column=2,sticky='nsew')
        
        
        
       
        self.label_status.configure(text='Próxima jogada: X', font='Arial 20 bold', fg = 'black')
        self.label_status.grid(row=3,column=0,columnspan=3)
        
   
              
        
                
    def botao0_0_clicado(self):              
        if self.jogo.jogador==1:
            letra='X'           
        else:
            letra='O'
        self.botao0_0.configure(text=letra,font='Arial 30 bold',state='disable')
        self.jogo.recebe_jogada(0,0)
        self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')
        self.ganhou()            
                
    def botao0_1_clicado(self):
         if self.jogo.jogador==1:
            letra='X'           
         else:
            letra='O'
         self.botao0_1.configure(text=letra,font='Arial 30 bold',state='disable')
         self.jogo.recebe_jogada(0,1)         
         self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')                  
         self.ganhou()

                
    def botao0_2_clicado(self):
        if self.jogo.jogador==1:
            letra='X'           
        else:
            letra='O'
        self.botao0_2.configure(text=letra,font='Arial 30 bold',state='disable')
        self.jogo.recebe_jogada(0,2)         
        self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')                 
        self.ganhou()

        
    def botao1_0_clicado(self):
         if self.jogo.jogador==1:
            letra='X'           
         else:
            letra='O'
         self.botao1_0.configure(text=letra,font='Arial 30 bold',state='disable')
         self.jogo.recebe_jogada(1,0)          
         self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')                 
         self.ganhou()
        
    def botao1_1_clicado(self):
        if self.jogo.jogador==1:
            letra='X'           
        else:
            letra='O'
        self.botao1_1.configure(text=letra,font='Arial 30 bold',state='disable')
        self.jogo.recebe_jogada(1,1)        
        self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')
                
        self.ganhou()
        
    def botao1_2_clicado(self):
         if self.jogo.jogador==1:
            letra='X'           
         else:
            letra='O'
         self.botao1_2.configure(text=letra,font='Arial 30 bold',state='disable')
         self.jogo.recebe_jogada(1,2)          
         self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')
                  
         self.ganhou()
        
    def botao2_0_clicado(self):
         if self.jogo.jogador==1:
            letra='X'           
         else:
            letra='O'
         self.botao2_0.configure(text=letra,font='Arial 30 bold',state='disable')
         self.jogo.recebe_jogada(2,0)           
         self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')
         self.ganhou()
        
    def botao2_1_clicado(self):
         if self.jogo.jogador==1:
            letra='X'           
         else:
            letra='O'
         self.botao2_1.configure(text=letra,font='Arial 30 bold',state='disable')
         self.jogo.recebe_jogada(2,1)         
         self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')
                   
         self.ganhou()

        
    def botao2_2_clicado(self):
         if self.jogo.jogador==1:
            letra='X'           
         else:
            letra='O'
         self.botao2_2.configure(text=letra,font='Arial 30 bold',state='disable')
         self.jogo.recebe_jogada(2,2)         
         self.label_status.configure(text=self.jogo.string_var,font='Arial 20 bold')
                   
         self.ganhou()


    def ganhou(self):
        if self.jogo.verifica_ganhador()==1:
            self.botao0_0.configure(state='disable')
            self.botao0_1.configure(state='disable')
            self.botao0_2.configure(state='disable')
            self.botao1_0.configure(state='disable')
            self.botao1_1.configure(state='disable')
            self.botao1_2.configure(state='disable')
            self.botao2_0.configure(state='disable')
            self.botao2_1.configure(state='disable')
            self.botao2_2.configure(state='disable')
            self.label_status.configure(text="X GANHOU",fg='blue')
            
        elif self.jogo.verifica_ganhador()==2:
            self.botao0_0.configure(state='disable')
            self.botao0_1.configure(state='disable')
            self.botao0_2.configure(state='disable')
            self.botao1_0.configure(state='disable')
            self.botao1_1.configure(state='disable')
            self.botao1_2.configure(state='disable')
            self.botao2_0.configure(state='disable')
            self.botao2_1.configure(state='disable')
            self.botao2_2.configure(state='disable')
            self.label_status.configure(text="O GANHOU",fg='red')
        
        elif self.jogo.verifica_ganhador()==0:
            self.label_status.configure(text='Deu VELHA')
        
            
            
        
    def iniciar(self):
        self.window.mainloop()
        
tab=Tabuleiro()
tab.iniciar()



    

              

    

              
