#definition of positional arguements with 2 examples
#    Positional arguements are needed to be included in proper order i.e, the first arguments is always listed first when the function is called ,second argument-
#needs to be called after the first argument and so on
# example of positional arguments:
def person_name(first_name,second_name):
    print(first_name+second_name)
    #first name is olafoyeku which is placed first
    #second name is gbenro which is placed after the first name
person_name("olafoyeku","gbenro")
#example 2
def add(a,b,c):
    addition=int(a)+int(b)+int(c)
    return addition
#first, during the function call , all arguments are given as positional arguments .Values-
#passed through arguments are passed to parameters by their position 10 is assigned to a, 20 is assigned to b, 30 is assigned to d
print(add(10,20,30))


#definition of keyword arguments with 2 examples:
#      keyword argument is an argument passed to a function or method which is preceded by a keyword and an equal to sign .The order of keyword argument with respect to another-
#keyword argument does not matter because the values are being explicitly assigned .

#example of a keyword argument:
def person_name(first_name,second_name):
    print(first_name + second_name)
# Here we are explicitly assigning the values
person_name(first_name="olafoyeku",second_name=" gbenro")
#example 2:
def add(a,b,c):
    addition=int(a)+int(b)+int(c)
    return addition
print(add(a=4,b=5,c=5))

# explanation on default arguments:
#-default arguments are values that are provided while defining functions.
#-the assignment operator = is used to assign a default value to the argument
#-default arguments become optional during the function calls 
#-if we provide a value to the default arguments during function calls , it overrides the default value

#example on default arguments
def add(a,b=5,c=10):
    return (a+b+c)
# giving only the mandatory arguments
print(add(3))

#giving one of the optional arguments
print(add(3,4))#3 is assigned to a, 4 assigned to b .Since when we provide a value to the default argument during function calls , it 
#overrides the default value.