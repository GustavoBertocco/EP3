#EP~Jogo da Velha
import tkinter as tk

class Tabuleiro:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("700x800+1000+1000")  
        self.window.title("Jogo da Velha")
        self.window.rowconfigure(0, minsize=100)
        self.window.rowconfigure(1, minsize=100)
        self.window.rowconfigure(2, minsize=100)
        self.window.rowconfigure(3, minsize=50)
        self.window.columnconfigure(0, minsize=100)
        self.window.columnconfigure(1, minsize=100)
        self.window.columnconfigure(2, minsize=100)
        
        
        self.botao0_0=tk.Button(self.window, padx=113.5,pady=105)
        self.botao0_0.configure(command=self.botao0_0_clicado)
        self.botao0_0.grid(row=0,column=0,sticky='nsew')
        
        self.botao0_1=tk.Button(self.window, padx=113.5,pady=105)
        self.botao0_1.configure(command=self.botao0_1_clicado)
        self.botao0_1.grid(row=0,column=1,sticky='nsew')
        
        self.botao0_2=tk.Button(self.window, padx=113.5,pady=105)
        self.botao0_2.configure(command=self.botao0_2_clicado)
        self.botao0_2.grid(row=0,column=2,sticky='nsew')
        
        self.botao1_0=tk.Button(self.window, padx=113.5,pady=105)
        self.botao1_0.configure(command=self.botao1_0_clicado)
        self.botao1_0.grid(row=1,column=0,sticky='nsew')
        
        self.botao1_1=tk.Button(self.window, padx=113.5,pady=105)
        self.botao1_1.configure(command=self.botao1_1_clicado)
        self.botao1_1.grid(row=1,column=1,sticky='nsew')
        
        self.botao1_2=tk.Button(self.window, padx=113.5,pady=105)
        self.botao1_2.configure(command=self.botao1_2_clicado)
        self.botao1_2.grid(row=1,column=2,sticky='nsew')
        
        self.botao2_0=tk.Button(self.window, padx=113.5,pady=105)
        self.botao2_0.configure(command=self.botao2_0_clicado)
        self.botao2_0.grid(row=2,column=0,sticky='nsew')
        
        self.botao2_1=tk.Button(self.window, padx=113.5,pady=105)
        self.botao2_1.configure(command=self.botao2_1_clicado)
        self.botao2_1.grid(row=2,column=1,sticky='nsew')
        
        self.botao2_2=tk.Button(self.window, padx=113.5,pady=105)
        self.botao2_2.configure(command=self.botao2_2_clicado)
        self.botao2_2.grid(row=2,column=2,sticky='nsew')
        
        self.label_status=tk.Label()
        self.label_status
        self.label_status.grid(row=3,column=0,columnspan=3)
        self.label_status.configure(text="Vez do Jogador")
    
        
            
        
        
    def botao0_0_clicado(self):
        self.botao_clicado(0,0)
        
    def botao0_1_clicado(self):
        self.botao_clicado(0,1)
                
    def botao0_2_clicado(self):
        self.botao_clicado(0,2)
        
    def botao1_0_clicado(self):
        self.botao_clicado(1,0)
        
    def botao1_1_clicado(self):
        self.botao_clicado(1,1)
        
    def botao1_2_clicado(self):
        self.botao_clicado(1,2)
        
    def botao2_0_clicado(self):
        self.botao_clicado(2,0)
        
    def botao2_1_clicado(self):
        self.botao_clicado(2,1)
        
    def botao2_2_clicado(self):
        self.botao_clicado(2,2)
        
    
        
    def iniciar(self):
        self.window.mainloop()
        
jogo=Tabuleiro()
jogo.iniciar()
        
        
        
        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
      

      