def addition():
    global num1
    global num2
    num1=float(input("enter the first value: "))
    num2=float(input("enter the second value: "))
    sum=num1+num2
    return sum
def subtraction():
    num1=float(input("enter the first value: "))
    num2=float(input("enter the second value: "))
    subtraction=num1-num2
    return subtraction
 

def choice():
    print("1 for addition ")
    print("2 for subtraction")
    choice=input(" Enter your choice either 1 or 2: ")
    if choice=="1":
        print(addition())
    elif choice=="2":
        print(subtraction())
    else:
        print(" pls insert a valid value either 1 or 2")
choice()



