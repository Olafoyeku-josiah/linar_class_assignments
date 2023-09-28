def user_info():
    global name
    name=input("  Pls enter your name: ")
    print("Hello {} ,welcome to gbenro's coaster biscuit depot".format(name))
    print("This program would be calculating total amount to be paid when you buy a particular size,quantity and type of coaster biscuits.")
    return name
user_info()
print("")
def total_amountpaid(coaster_type,carton_quantity,carton_size):
    coaster_type1="50 naira"
    """the variable coaster_type1 stores the type of coaster biscuit the user would like to buy 
    and it stores the big type of coaster biscuit"""
    coaster_type2="20 naira"
    """this variable coaster_type2 also stores the type of coaster biscuit the user would like to buy
    annd it stores the small type of coaster biscuit"""
    small_carton_quantity=45 # for the big type
    medium_carton_quantity= 75 # for the big type
    large_carton_quantity=110 #for the big type
    small_carton_quantity1=65 # for the small type
    medium_carton_quantity2=100# for the small type
    large_carton_quantity3=140 # for the small type
    small_carton_cost=4000 # fixed price for both coaster types
    medium_carton_cost=5500 # fixed price for both coaster types
    large_carton_cost= 7000 # fixed price for both coaster types
    if coaster_type==coaster_type1 and carton_size=="small":
        amount1=int(carton_quantity) * int(small_carton_cost)/ int(small_carton_quantity)
        print(" The total amount to be paid for the small carton size of the 50naira coaster biscuit is: {:.0f}naira ".format(amount1))
# if carton quantity is specified by the user then we can calculate number of carton to be bought by the customer and also asking for carton size
        if carton_quantity== carton_quantity:
            number_of_cartons=input(" since we sell in bulk would you like to buy more cartons of biscuit (yes or no): ")
            if number_of_cartons=="yes":
                carton_spec=input(" if yes,what carton size would you like to buy(small,medium,large): ")
                carton_numbers=int(input(" Enter the number of cartons you would like to buy: "))
                if carton_spec=="small":
                    global carton_cost
                    carton_cost=carton_numbers*amount1
                    print(" The amount to be paid for the small carton size is: {:.0f}naira".format(carton_cost))
                elif carton_spec=="medium":
                    carton_cost_c=carton_numbers*medium_carton_cost
                    total_cost_a=carton_cost_c+amount1
                    print(" the total amount to be paid for the medium carton size is: {}naira".format(carton_cost_c))
                    print(" Therefore the total cost after purchasing is {}naira".format(total_cost_a))
                elif carton_spec=="large":
                    carton_cost_d=carton_numbers*large_carton_cost
                    total_cost_b=carton_cost_d+amount1
                    print(" the amount to be paid for the large carton size is: {}naira ".format(carton_cost_d))
                    print(" Therefore the total cost after purchasing is {}naira".format(total_cost_b))
            if number_of_cartons=="no":
                print(" Dear {} since you are not buying in bulk your total cost still small carton size remains the same .\n Thank you for purchasing at gbenro's coaster biscuit depot ".format(name))
    elif coaster_type==coaster_type1 and carton_size=="medium":
        amount2=int(carton_quantity) * int(medium_carton_cost)/ int(medium_carton_quantity)
        print(" The total amount to be paid for the medium carton size of the 50naira coaster biscuit is: {:.0f}naira ".format(amount2))
        if carton_quantity==carton_quantity:
                number_of_cartons2=input(" since we sell in bulk would you like to buy more cartons of biscuit (yes or no): ")
                if number_of_cartons2=="yes":
                    carton_spec2=input(" if yes, what carton size would you like to buy(small,medium,large): ")
                    carton_numbers2=int(input(" Enter the number of cartons you would like to buy: "))
                    if carton_spec2=="medium":
                        carton_cost2=carton_numbers2*amount2
                        print(" The amount to be paid for the medium carton size is: {:.0f}naira ".format(carton_cost2))
                    elif carton_spec2=="small":
                        carton_cost_a=carton_numbers2*small_carton_cost
                        total_cost_c=carton_cost_a+amount2
                        print(" The amount needed to buy the small carton size is {}naira ".format(carton_cost_a))
                        print(" Therefore the total cost after purchasing is {}naira".format(total_cost_c))
                    elif carton_spec2=="large":
                        carton_cost_b=carton_numbers2*large_carton_cost
                        total_cost_d=carton_cost_b+amount2
                        print("  The amount needed to buy the large carton size is {}naira".format(carton_cost_b))
                        print(" Therefore the total cost after purchasing is {}naira".format(total_cost_d))
                if number_of_cartons2=="no":
                    print(" Dear {} since you are not buying in bulk your total cost for medium carton size still remains the same .\n Thank you for purchasing at gbenro's coaster biscuit depot ".format(name))
    elif coaster_type==coaster_type1 and carton_size=="large":
        amount3=int(carton_quantity) * int(large_carton_cost)/int(large_carton_quantity)
        print(" The total amount to be paid for the large carton size of the 50naira coaster biscuit is: {:.0f}naira ".format(amount3))
        if carton_quantity==carton_quantity:
            number_of_cartons3=input(" Since we sell in bulk would you like to buy more cartons of biscuit(yes or no): ")
            if number_of_cartons3=="yes":
                carton_spec3=input(" if yes, what carton size would you like to buy(small,medium,large): ")
                carton_numbers3=int(input(" Enter the number of cartons you would like to buy: "))
                if carton_spec3=="large":
                      carton_cost3a=carton_numbers3*amount3
                      print(" the amount to be paid for the large carton size is: {:.0f}naira".format(carton_cost3a))
                elif carton_spec3=="medium":
                    carton_cost3b=carton_numbers3*medium_carton_cost
                    total_cost_e=carton_cost3b+amount3
                    print(" the amount to be paid for the medium carton size is: {:.0f}naira".format(carton_cost3b))
                    print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_e))
                elif carton_spec3=="small":
                      carton_cost3c=carton_numbers3*small_carton_cost
                      total_cost_f=carton_cost3c+amount3
                      print(" the amount to be paid for the small carton size is: {:.0f}naira".format(carton_cost3c))
                      print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_f))
            if number_of_cartons3=="no":
                print(" Dear {} since you are not buying in bulk your total cost for large carton size still remains the same .\n Thank you for purchasing at gbenro's coaster biscuit depot ".format(name))
    elif coaster_type==coaster_type2 and carton_size=="small":
        amount4=int(carton_quantity) * int(small_carton_cost)/int(small_carton_quantity1)
        print(" The total amount to be paid for the small carton size of the 20naira coaster biscuit is: {:.0f}naira ".format(amount4))
        if carton_quantity==carton_quantity:
            number_of_cartons4=input(" Since we sell in bulk would you like to buy more cartons of biscuit(yes or no): ")
            if number_of_cartons4=="yes":
                carton_spec4=input(" if yes, what carton size would you like to buy(small,medium,large): ")
                carton_numbers4=int(input(" Enter the number of cartons you would like to buy: "))
                if carton_spec4=="large":
                      carton_cost4=carton_numbers4*amount4
                      print(" the amount to be paid for the large carton size is: {:.0f}naira".format(carton_cost4))
                elif carton_spec4=="medium":
                    carton_cost4b=carton_numbers4*medium_carton_cost
                    total_cost_g=carton_cost4+amount4
                    print(" the amount to be paid for the medium carton size is: {:.0f}naira".format(carton_cost4b))
                    print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_g))
                elif carton_spec4=="small":
                      carton_cost4c=carton_numbers4*small_carton_cost
                      total_cost_h=carton_cost4b+amount4
                      print(" the amount to be paid for the small carton size is: {:.0f}naira".format(carton_cost4c))
                      print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_h))
            if number_of_cartons4=="no":
                print(" Dear {} since you are not buying in bulk your total cost for the 20 naira coaster quantity still remains the same .\n Thank you for purchasing at gbenro's coaster biscuit depot ".format(name))
    elif coaster_type==coaster_type2 and carton_size=="medium":
        amount5=int(carton_quantity) * int(medium_carton_cost)/int(medium_carton_quantity2)
        print(" The total amount to be paid for the medium carton size of the 20naira coaster biscuit is: {:.0f}naira ".format(amount5))
        if carton_quantity==carton_quantity:
            number_of_cartons5=input(" Since we sell in bulk would you like to buy more cartons of biscuit(yes or no): ")
            if number_of_cartons5=="yes":
                carton_spec5=input(" if yes, what carton size would you like to buy(small,medium,large): ")
                carton_numbers5=int(input(" Enter the number of cartons you would like to buy: "))
                if carton_spec5=="large":
                      carton_cost5a=carton_numbers5*amount5
                      print(" the amount to be paid for the large carton size is: {}naira".format(carton_cost5a))
                elif carton_spec5=="medium":
                    carton_cost5b=carton_numbers5*medium_carton_cost
                    total_cost_i=carton_cost5b+amount5
                    print(" the amount to be paid for the medium carton size is: {}naira".format(carton_cost5b))
                    print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_i))
                elif carton_spec5=="small":
                      carton_cost5c=carton_numbers5*small_carton_cost
                      total_cost_j=carton_cost5c+amount5
                      print(" the amount to be paid for the small carton size is: {}naira".format(carton_cost5c))
                      print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_j))
            if number_of_cartons5=="no":
                print(" Dear {} since you are not buying in bulk your total cost for the 20 naira coaster quantity still remains the same .\n Thank you for purchasing at gbenro's coaster biscuit depot ".format(name))
    elif coaster_type==coaster_type2 and carton_size=="large":
        amount6=int(carton_quantity) * int(large_carton_cost)/int(large_carton_quantity3)
        print(" The total amount to be paid for the large carton size of the 20naira coaster biscuit is: {:.0f}naira ".format(amount6))
        if carton_quantity==carton_quantity:
            number_of_cartons6=input(" Since we sell in bulk would you like to buy more cartons of biscuit(yes or no): ")
            if number_of_cartons6=="yes":
                carton_spec6=input(" if yes, what carton size would you like to buy(small,medium,large): ")
                carton_numbers6=int(input(" Enter the number of cartons you would like to buy: "))
                if carton_spec6=="large":
                      carton_cost6a=carton_numbers6*amount6
                      print(" the amount to be paid for the large carton size is: {}naira".format(carton_cost6a))
                elif carton_spec6=="medium":
                    carton_cost6b=carton_numbers6*medium_carton_cost
                    total_cost_k=carton_cost6b+amount6
                    print(" the amount to be paid for the medium carton size is: {}naira".format(carton_cost6b))
                    print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_k))
                elif carton_spec6=="small":
                      carton_cost6c=carton_numbers6*small_carton_cost
                      total_cost_l=carton_cost6c+amount6
                      print(" the amount to be paid for the small carton size is: {}naira".format(carton_cost6c))
                      print(" Therefore the total cost after purchasing is {:.0f}naira".format(total_cost_l))
            if number_of_cartons6=="no":
                print(" Dear {} since you are not buying in bulk your total cost for the 20 naira coaster quantity still remains the same .\n Thank you for purchasing at gbenro's coaster biscuit depot ".format(name))
    else :
        print(" Dear user, pls input the correct coaster type or quantity and carton size.")
    return 
total_amountpaid(coaster_type=input("Pls enter the coaster type whether the big type(50 naira) or the small type(20 naira) of coaster: "),carton_quantity=input("Pls enter the quantity of biscuits in a carton: "),carton_size=input("Pls enter carton size whether small,medium or large: "))
        