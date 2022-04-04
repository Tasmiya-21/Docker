import pytest

def max(values):
    max=values[0]
    #print(values[0])
    for val in values:
        if val>max:
            max=val
    #print("The maximum number is",max)
    return max
    
def min(values):
    min=values[0]
    for val in values:
        if val<min:
            min=val
    #print("The minimum number is",min)
    return min
def test_max():
    values=eval(input("enter your list: "))
    #values=[4,87,10,2]
    assert max(values)==int(input("enter your no1:"))

def test_min():
    values=eval(input("enter your list: "))
    #values=[4,87,10,2]
    assert min(values)==int(input("enter your no2:"))

#values=[4,87,10,2]
   
#max(values)
#min(values)
#test_method()
