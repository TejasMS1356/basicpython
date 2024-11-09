import random
print("WELCOME TO THE GAME.......READY TO PLAY")
rno=random.randint(0,1)


while(True):
      
     
      a=int(input("enter the no in the range of 0 to 1000: "))
      if a<0 or a>1000:
            print("enter the no in the range of 0 to 1000")
      elif a==rno:
            print(f"congragulations you won the game!!!!!! the no is {rno}")
            
            d=int(input("1.continue \n 2. exit: "))
            if d==1:
                  continue
            elif d==2:
                   break
            
      
            
      elif a>rno:
             print(f"guess the no less than {a}")
      elif  a<rno:
             print(f"guess the no greater than {a}")
      
                  
                         
           
      
      