def Calculator(val_1,val_2):
    flag=True
    while(flag):
        
        choice=input("Which calculation You Want To Perfom(Add,Sub,Mul,Div,stop): ")
        
        if choice == "Add":
            print(f"The addition of {val_1} and {val_2} is {val_1+val_2}")
        elif choice == "Sub":
            print(f"The subtraction of {val_1} and {val_2} is {val_1-val_2}")
        elif choice == "Mul":
            print(f"The multiplication of {val_1} and {val_2} is {val_1*val_2}")
        elif choice == "Div":
            try:
                print(f"The division of {val_1} and {val_2} is {val_1/val_2}")
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
    

#Arithmatic(60,25)
Arithmatic(int(input("enter first number: ")),int(input("enter second number: ")))

