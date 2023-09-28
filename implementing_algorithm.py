#accepting variables l,f,w,n,s from the user to solve the mathematical problem
formula_variable1=int(input("enter the values for the variable L:"))
print("the value for L is: {}".format(formula_variable1))

formula_variable2=int(input("enter the values for the variable f:"))
print("the value for f is: {}".format(formula_variable2))

formula_variable3=int(input("enter the values for the variable w:"))
print("the value for L is: {}".format(formula_variable3))

formula_variable4=int(input("enter the values for the variable n:"))
print("the value for n is: {}".format(formula_variable4))

formula_variable5=int(input("enter the values for the variable s:"))
print("the value for s is: {}".format(formula_variable5))

numerator_value_calA=pow(formula_variable2,formula_variable3)
numerator_value_calB=formula_variable5 * formula_variable1 / formula_variable2
new_const1=20

formula_value_calC=new_const1 / formula_variable2

formula_value_calD=pow(formula_value_calC,formula_variable4)
denominator_value_calE=pow(new_const1,formula_variable3)
denominator_value_calF=pow(formula_variable2,0.5)

final_numeratorcal=numerator_value_calB + formula_value_calD
final_denominatorcal=denominator_value_calE + denominator_value_calF
numerator_denominatorcal=numerator_value_calA * final_numeratorcal / final_denominatorcal

final_calculation_Y=formula_variable1 - numerator_denominatorcal
formula_final_calculationY=int(final_calculation_Y)
print("the final result for the problem Y after substitution of values= {}".format(formula_final_calculationY))

