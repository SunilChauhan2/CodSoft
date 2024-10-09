#Heading
print("               CALCULATOR           ")

#Input Numbers
A=int(input("Enter first number: "))  
B=int(input("Enter second number: "))

#function for calculation
def operations (A,B):
    if (x== "+"):
        print(A+B)
    elif(x== "-"):
        print(A-B)
    elif(x== "/"):
        print(A/B)
    elif(x== "*"):
        print(A*B)
    else:
        print("INVALID INPUT")

#Operation 
x=input("Chose Operation (+,-,/,*) : ")
#function call
operations(A,B)
print("Thanks For Calculating 45:)")
