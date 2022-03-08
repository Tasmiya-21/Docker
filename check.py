#text=input("Enter your text :")
text="short-gun"
l=["short-gun","rifle","pistol","uzi"]
count=0
for i in text.split():
    
    if i in l:
        count+=1
if count>0:
        
    print("This is bad word in the string")
    
else:
    print("This is good word in the string")
