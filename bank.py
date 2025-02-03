#DICTIONARY OF ACCOUNT NO AND AMOUNT
d = {
        12345678: 45000,
        23456789: 36789
    }
#ANOTHER DICTIONARY OF ACC NO AND IFSC CODE
ifsccode={
       12345678 :"WERTY6373",
       23456789 :"asdfg3454"
    }
#FUNCTION TO CHECKA AND PRINT THE AMOUNT
def bank(ac, ifsc):
    if ac in d and ifsc == ifsccode.get(ac):
        print("THE AMOUNT PRESENT IN ACC IS:",d[ac])
       
        return True,d
    else:
        print("Not matching")
        print("Try again! You have 3 attempts")
        return False,d
print("**** WELCOME TO AMOUNT CHECKING SOFTWARE*****")
i = 0
#WHILE LOOP FOR ENTERING THE CORRECT ACC NO
while i<3:
    
    ac = int(input("Enter YOUR CORRECT ACCOUNTNUMBER: "))
    ifsc = input("Enter the IFSC code(IN CAPITALS): ").upper()
    r,d=bank(ac, ifsc)
    
    if r:
        #WHILE LOOP FOR CONTINIOUS TRANSACTIONS
        while True:
            s=input("ENTER THE CHOICE CREDIT/DEBIT(1/2):")
            if s=="1":
                c=int(input("ENTER THE AMOUNT TO CREDIT  IN YOUR BANK ACCOUNT: "))
                d[ac]+=c
                print("NEW BALANCE  IS ",d[ac])
            elif s=="2":
                c=int(input("ENTER THE AMOUNT TO BE WITHDRAWAL: "))
                if c>d[ac]:
                        print("please enter the amount less than the amount in the balance")
                        print("CURRENT BALANCE: ",d[ac])
                else:
                        d[ac]-=c
                        print("CURRENT BALANCE: ",d[ac])
            k=int(input("ENTER 3  TO CONTINUE THE TRANSACTION OR 4 TO EXIT: "))
            if k!=3:
                print("CURRENT BALANCE IS:",d[ac])
                print("****THANK YOU! VISIT AGAIN*****")
                break
        break
    i+=1


        
        
    
   
        

