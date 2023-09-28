#also using the is_integer method to check whether a value is a float or an integer
number=3.55
if number.is_integer()==True:
    print("{} is an integer.".format(number))
elif number.is_integer()!=True:
    print("{} is a float".format(number))
else:
    print("this is a string")

#using the _round_ method to round a float to a specified number of decimal places
decimal_number=3.14159
approximated_number=decimal_number.__round__(2)
print(approximated_number)

#using the _trunc_ method to return the integral part of a float as an integer
decimal_number=3.14159
integer_value=decimal_number.__trunc__()
print(integer_value)

#using the _ceil_() method to return the smallest integer greater than or equal to a float
decimal_number=4.56
integer_value=decimal_number.__ceil__()
print(integer_value)
