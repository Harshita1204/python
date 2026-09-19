def greet():
    print("Hello")
greet()

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

#we are defining the variable inside the function-> locally  that is why there will not be any error of the variables
# if you want to access the variables then you have to define it somewhere too to access it globally
def add(a,b):
    return a+b 

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b  

def calculate(a,b):
    sum= add(10,20)  
    diff= sub(10,5)
    prod= mul(10,20)
    print(f"sum = {sum} difference = {diff} product = {prod} \n ")
calculate(10,20)    
