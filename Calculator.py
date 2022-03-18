def Arithmatic(val_1,val_2):
    flag=True
    while(flag):
        
        choice=input("Which calculation You Want To Perfom(Add,Sub,Mul,Div,stop): ")
        
        if choice == "Add":
            print(val_1 + val_2)
        elif choice == "Sub":
            print(val_1 - val_2)
        elif choice == "Mul":
            print(val_1 * val_2)
        elif choice == "Div":
            try:
                print(val_1 / val_2)
            except:
                print("Denominator cannot be zero")
        elif choice=="stop":
            flag = False
       
        else:
            print("enter correct choice")
            flag=True
        n=input("Do you want to continue Yes/No: ")
        if n=="Yes":
            flag=True
        else:
            flag=False
    

Arithmatic(int(input("enter first number:")),int(input("enter second number:")))
