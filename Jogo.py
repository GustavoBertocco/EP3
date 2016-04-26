import numpy as np
class Jogo:
    def __init__(self):
        self.jogadas=1
        self.a=np.zeros((3,3))
        self.jogador=1
        self.string_var='Próxima jogada: X'
     
        
        
    def recebe_jogada(self,linha, coluna):        
       self.a[linha][coluna]=self.jogador
       if self.jogador==1:
           self.jogador=4
           self.string_var='Próxima jogada: O'
           
       elif self.jogador==4:
           self.jogador=1
           self.string_var='Próxima jogada: X'

   #Funções Jogo



    def verifica_ganhador(self):
    
    # X vence!!
        if self.a[0][0] + self.a[1][0] + self.a[2][0] == 3 or\
           self.a[0][0] + self.a[1][1] + self.a[2][2] == 3 or\
           self.a[0][0] + self.a[0][1] + self.a[0][2] == 3 or\
           self.a[1][0] + self.a[1][1] + self.a[1][2] == 3 or\
           self.a[2][0] + self.a[2][1] + self.a[2][2] == 3 or\
           self.a[2][0] + self.a[1][1] + self.a[0][2] == 3 or\
           self.a[0][1] + self.a[1][1] + self.a[2][1] == 3 or\
           self.a[0][2] + self.a[1][2] + self.a[2][2] == 3 :
               return 1                                      
            
    # O vence! !
        elif self.a[0][0] + self.a[1][0] + self.a[2][0] == 12 or\
             self.a[0][0] + self.a[1][1] + self.a[2][2] == 12 or\
             self.a[0][0] + self.a[0][1] + self.a[0][2] == 12 or\
             self.a[1][0] + self.a[1][1] + self.a[1][2] == 12 or\
             self.a[2][0] + self.a[2][1] + self.a[2][2] == 12 or\
             self.a[2][0] + self.a[1][1] + self.a[0][2] == 12 or\
             self.a[0][1] + self.a[1][1] + self.a[2][1] == 12 or\
             self.a[0][2] + self.a[1][2] + self.a[2][2] == 12 :
            return 2
    #Velha
            
        elif  self.a[0][0] + self.a[1][0] + self.a[2][0] +\
              self.a[0][1] + self.a[1][1] + self.a[2][1] +\
              self.a[0][2] + self.a[1][2] + self.a[2][2]==21:
              return 0
            
        else:
            return -1
        
        
       
