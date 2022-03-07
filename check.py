text=input("Enter your text :")
l=["gun","ruffle","pistol","s"]
count=0
for i in text.split():
    
    if i in l:
        count+=1
if count>0:
        
    print("This is bad")
    
else:
    print("This is good")
