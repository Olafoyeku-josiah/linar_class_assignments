#program to calculate and give the final result of the mathematical problem 5a+(3b)^2

print("calculating 5a+(3b)^2:")
first_value=int(input("enter value for a:")) #accept input from user for value a
second_value=int(input("enter value for b:")) #accept input from user for value b
value_x="3" #storing the co-efficient of "b" in a variable called value_x
value_y="5" #storing the co-efficient of "a" in a variable called value_x

new_value_x=int(value_x) #converting the co-efficient of "b" from string to integer data type
new_value_y=int(value_y) #converting the co-efficient of "a" from string to integer data type

square_of_value=new_value_x*pow(second_value,2) #multiplying the co-efficient of "b" by the square of "b"
print("the square of the problem ((3b)^2) is: "+str(square_of_value)+" therefore the final value is:")
first_value_calx=new_value_y * first_value #multiplying the co-efficient of "a" by "a"
cal_finalresult=first_value_calx + square_of_value #calculating the final result of the mathematical problem
print("5a+(3b)^2= "+str(cal_finalresult)) #printing the final result

