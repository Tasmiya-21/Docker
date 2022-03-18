def Calculator(val_1,val_2):
    flag=True
    while(flag):
        
        choice=input("Which calculation You Want To Perfom(Add,Sub,Mul,Div,stop): ")
        
        if choice == "Add":
            print("The addition of two numbers is", val_1+val_2)
        elif choice == "Sub":
             print("The subtraction of two numbers is", val_1-val_2)
        elif choice == "Mul":
            print("The multiplication of two numbers is", val_1*val_2)
        elif choice == "Div":
            try:
              print("The division of two numbers is", val_1/val_2)
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
    
Calculator(int(input("enter first number: ")),int(input("enter second number: ")))
