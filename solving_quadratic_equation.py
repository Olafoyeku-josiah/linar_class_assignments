"""this code is used to solve quadratic formula by accepting inputs from the user"""
user_name=input("enter your name pls: ")
print("HI {}".format(user_name))
print("This program will be calculating the quadratic formula testing with values 2,3,-1: ")
print("")
value_a=float(input(" Enter the first value a: "))
value_b=float(input(" Enter the second value b: "))
value_c=float(input(" Enter the third value c: "))

numerator_value1=value_a * value_c
const1=4
const2=2
value_1b=const1 * numerator_value1
numerator_value2=pow(value_b,2)
right_hand_side_value=numerator_value2 - value_1b
numerator_section=pow(right_hand_side_value,0.5)
left_hand_side_value=  -(value_b)
positive_valueX=left_hand_side_value + numerator_section
negative_valueX=left_hand_side_value - numerator_section
denominator_value=const2 * value_a

total_X=positive_valueX / denominator_value
total_X2=negative_valueX / denominator_value

print("the solution for the quadratic equation using 2,3,-1 is: ")
print("the value for X is {:.2f} or {:.2f}".format(total_X,total_X2))