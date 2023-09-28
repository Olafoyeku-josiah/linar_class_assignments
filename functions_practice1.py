#multiple functions to calculate total volume of three solid shapes..
"""def name(user_name):
    user_name=input("Enter your name: ")
    print("HI {}".format(user_name))
name(name)

def first_volume(length,height,breadth):
    length=input(" Enter the length of the first solid shape: ")
    height=input(" Enter the height for the first solid shape: ")
    breadth=input(" Enter the breadth for the first soild shape: ")
    volume=int(length)*int(height)*int(breadth)
    return volume
print("")

def second_volume(length,height,breadth):
    length=input(" Enter the length of the second solid shape: ")
    height=input(" Enter the height for the second solid shape: ")
    breadth=input(" Enter the breadth for the second soild shape: ")
    volume=int(length)*int(height)*int(breadth)
    return volume
print("")

def third_volume(length,height,breadth):
    length=input(" Enter the length of the third solid shape: ")
    height=input(" Enter the height for the third solid shape: ")
    breadth=input(" Enter the breadth for the third soild shape: ")
    volume=int(length)*int(height)*int(breadth)
    return volume
print("")"""




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



