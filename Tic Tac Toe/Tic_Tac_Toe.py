import os

class TicTacToe:
    Chk=list()
    Chk=[""]*9 


    def __init__(self):
       #Chk=[" "]*9   #All positions are empty at the start of game
       pass
     

    def displayBoard(self):
       print("",self.Chk[0]," ",self.Chk[1]," ",self.Chk[2])
       print("___|___|___")
       print("",self.Chk[3]," ",self.Chk[4]," ",self.Chk[5])
       print("___|___|___")
       print("",self.Chk[6]," ",self.Chk[7]," ",self.Chk[8])
       print("   |   |   ")

    def Winnings(self,char):
        Win=False
        if self.Chk[0]==char and self.Chk[1]==char and self.Chk[2]==char:     #1st Horizontal 
            Win=True
        elif self.Chk[3]==char and self.Chk[4]==char and self.Chk[5]==char:   #2nd Horizontal
            Win=True
        elif self.Chk[6]==char and self.Chk[7]==char and self.Chk[8]==char:   #3rd Horizontal
            Win=True
        elif self.Chk[0]==char and self.Chk[3]==char and self.Chk[6]==char:   #1st Vertical
            Win=True
        elif self.Chk[1]==char and self.Chk[4]==char and self.Chk[7]==char:   #2nd Vertical
            Win=True
        elif self.Chk[2]==char and self.Chk[5]==char and self.Chk[8]==char:   #3rd Vertical
            Win=True
        elif self.Chk[0]==char and self.Chk[4]==char and self.Chk[8]==char:   #Forward Diagnol
            Win=True
        elif self.Chk[2]==char and self.Chk[4]==char and self.Chk[6]==char:   #Reverse Diagnol
            Win=True
        return Win

    def Poss(self,Choice1):
        Available=False
        if self.Chk[Choice1-1]=="":
            Available=True
        return Available

    def tieCondition(self):
        flag=True
        for x in self.Chk:
            if x=="":
                flag=False
        if flag:
            print("The Game has been Tie")
            exit(0)

    def ChooseOption(self):
        num=1           #X for Player01 and 0 for Player02 

        while(1):
            os.system("cls")
            self.displayBoard()
            print("Player 0"+str(num)+" Turn: ")
            Choice= int(input())
            Yes=self.Poss(Choice)
            if Yes==True:
                if num==1:
                     self.Chk[Choice-1]='X'
                     if self.Winnings('X')==True:
                         print("Player 01 has Won the Game!!!")
                         self.displayBoard()
                         break
                     else:
                         self.tieCondition()
                     num=2
                else:
                     self.Chk[Choice-1]='0'
                     if self.Winnings('0')==True:
                         print("Player 02 has Won the Game!!!")
                         self.displayBoard()
                         break
                     else:
                         self.tieCondition()
                     num=1
            else:
               print("Space is already occupied, Choose a different Box!!")
               continue
           

      



Obj1 = TicTacToe()
#Obj1.displayBoard()
Obj1.ChooseOption()