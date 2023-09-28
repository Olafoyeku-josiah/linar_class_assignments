#using the _add_ method to add two integers together instead of using the '+' operator
a=4
b=5
result=a.__add__(b)#alternatively ,you can use the shorthand a+b
print(result)

#using the bin() method to convert an integer to its binary representation
num=10
binary=bin(num)[2:]#using the index to remove the ob prefix 
print(binary)

#using the bit_length method to return the number of bits required to represent an integer
num=42
length=num.bit_length()
print(length)

#using the to_byte to convert an integer into a byte representation 
num=42
byte_representation=num.to_bytes(2,byteorder='big')
print(byte_representation)
#it takes two arguments : length and byteorder the length argument specifies the number of bytes to use for the representation
# and the byteorder arguments specifies the byteorder either big or little

#using the is_integer to check if a particular value is a float or an integer 
num=3.0
if num.is_integer()==True:
    print("{} is an integer".format(num))
elif num.is_integer()!=True:
    print("{} is not an integer".format(num))
else:
    print("it is a string..")