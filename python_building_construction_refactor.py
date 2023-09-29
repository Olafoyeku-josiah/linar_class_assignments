#this function is embedded with the introduction and welcome and also user name
def introduction():
    global user_name
    user_name=input("Enter your name pls: ")
    print("Hello {}".format(user_name))
    print("Welcome to gbenro's building construction evaluation.")
    print("This program will be calculating your total number of blocks and building expenses using two different block sizes.")
    print("   Calculating number of blocks and expense required using smaller brick A and bigger brick B")
introduction()
print("")
room_height_const=12
length=1.25 #block A length value converted from inches to feet
height=0.75 #block A height value converted from inches to feet
cost=600 # cost of smaller brick A 
brickA_length=float(length)
brickA_height=float(height)
brickA_cost=int(cost)
#bigger brick b dimensions in feets
length=1.67 #blockB length value when converted from inches to feets
height=1 #block B height value when converted from inches to feets
cost=1000 #cost of larger brick B
brickB_length=float(length)
brickB_height=float(height)
brickB_cost=int(cost)
#building evaluation using the def function
def room1_calculation():
    user_room1_length=float(input(" Enter the length for room 1: "))
    user_room1_breadth=float(input(" Enter the breadth for room 1: "))
    room1_wall1=user_room1_length / brickA_length
    round_value1=round(room1_wall1)+1
    room1_wall1_height=room_height_const / brickA_height
    No_of_blocks_for_wall1=round_value1*room1_wall1_height * 2
    room1_wall2=user_room1_breadth / brickA_length
    round_value2=round(room1_wall2) +1
    room1_wall2_height=room_height_const / brickA_height
    No_of_blocks_for_wall2=round_value2 * room1_wall2_height * 2
    global blocks_total_for_room_1
    blocks_total_for_room_1=No_of_blocks_for_wall1 + No_of_blocks_for_wall2
    new_room1_wall1=user_room1_length / brickB_length
    roundvalue1=round(new_room1_wall1)+1
    room1_wall1_height=room_height_const / brickB_height
    No_of_blocks_for_new_wall1=roundvalue1 * room1_wall1_height * 2
    new_room1_wall2=user_room1_breadth /brickB_length
    roundvalue2=round(new_room1_wall2)+1
    room1_wall2_height=room_height_const / brickB_height
    No_of_blocks_for_new_wall2=roundvalue2 * room1_wall2_height * 2
    global blocks_total_for_first_room
    blocks_total_for_first_room=No_of_blocks_for_new_wall1 + No_of_blocks_for_new_wall2
    print(" The total number of blocks for room 1 using smaller brick A is {:.0f} blocks and using bigger brick B is {:.0f} blocks".format(blocks_total_for_room_1,blocks_total_for_first_room))
    return 
room1_calculation()
print("")
def room2_calculation():
    user_room2_length=float(input(" Enter the length for room 2: "))
    user_room2_breadth=float(input(" Enter the breadth for room 2: "))
    #calculation for total number of blocks using smaller brick A and bigger brick B for room 2 
    room2_wall1=user_room2_length / brickA_length
    round_value2=round(room2_wall1)+1
    room2_wall1_height=room_height_const / brickA_height
    No_of_blocks_for_room2_wall1=round_value2*room2_wall1_height * 2
    room2_wall2=user_room2_breadth / brickA_length
    round_value3=round(room2_wall2) +1
    room2_wall2_height=room_height_const / brickA_height
    No_of_blocks_for_room2_wall2=round_value3 * room2_wall2_height * 2
    global blocks_total_for_room_2
    blocks_total_for_room_2=No_of_blocks_for_room2_wall1 + No_of_blocks_for_room2_wall2
    new_room2_wall1=user_room2_length / brickB_length
    roundvalue3=round(new_room2_wall1)+1
    room2_wall1_height=room_height_const / brickB_height
    No_of_blocks_for_new_room2_wall1=roundvalue3* room2_wall1_height *2
    new_room2_wall2=user_room2_breadth / brickB_length
    roundvalue4=round(new_room2_wall2)+1
    room2_wall2_height=room_height_const / brickB_height
    No_of_blocks_for_new_room2_wall2=roundvalue4 * room2_wall2_height * 2
    global blocks_total_for_second_room
    blocks_total_for_second_room=No_of_blocks_for_new_room2_wall1 + No_of_blocks_for_new_room2_wall2
    print(" The total number of blocks for room 2 using smaller block A is {:.0f} blocks and using bigger brick B is {:.0f} blocks. ".format(blocks_total_for_room_2,blocks_total_for_second_room))
room2_calculation()
print("")
def room3_calculation():
    user_room3_length=float(input(" Enter the length for room 3: "))
    user_room3_breadth=float(input(" Enter the breadth for room 3: "))
#calculation for total number of blocks using smaller brick A and bigger brick B for room 3
    room3_wall1=user_room3_length / brickA_length
    round_value4=round(room3_wall1)+1
    room3_wall1_height=room_height_const / brickA_height
    No_of_blocks_for_room3_wall1=round_value4 * room3_wall1_height*2
    room3_wall2=user_room3_breadth / brickA_length
    round_value5=round(room3_wall2)+1
    room3_wall2_height=room_height_const / brickA_height
    No_of_blocks_for_room3_wall2=round_value5 * room3_wall2_height*2
    global blocks_total_for_room_3
    blocks_total_for_room_3=No_of_blocks_for_room3_wall1 + No_of_blocks_for_room3_wall2
    new_room3_wall1=user_room3_length / brickB_length
    roundvalue5=round(new_room3_wall1)+1
    room3_wall1_height=room_height_const / brickB_height
    No_of_blocks_for_new_room3_wall1=roundvalue5 * room3_wall1_height*2
    new_room3_wall2=user_room3_breadth / brickB_length
    roundvalue6=round(new_room3_wall2)+1
    room3_wall2_height=room_height_const / brickB_height
    No_of_blocks_for_new_room3_wall2=roundvalue6 * room3_wall2_height*2
    global blocks_total_for_third_room
    blocks_total_for_third_room=No_of_blocks_for_new_room3_wall1 + No_of_blocks_for_new_room3_wall2
    print("Mr/Mrs {} the total number of blocks for room 3 using smaller brick A is {:.0f} blocks and using bigger brick B is {:.0f} blocks. ".format(user_name,blocks_total_for_room_3,blocks_total_for_third_room))
room3_calculation()
print("")
def toilet_evaluation():
    user_toilet_length=float(input(" Enter the length for the toilet: "))
    user_toilet_breadth=float(input(" Enter the breadth for the toilet: "))

#total number of blocks for the toilet using smaller brick A and bigger brick B
    toilet_wall1=user_toilet_length / brickA_length
    round_value6=round(toilet_wall1)+1
    toliet_wall1_height=room_height_const / brickA_height
    no_of_blocks_for_toilet_wall1=round_value6 * toliet_wall1_height*2

    toilet_wall2=user_toilet_breadth / brickA_length
    round_value7=round(toilet_wall2)+1
    toliet_wall2_height=room_height_const / brickA_height
    no_of_blocks_for_toilet_wall2=round_value7 * toliet_wall2_height*2
    global blocks_total_for_toilet
    blocks_total_for_toilet=no_of_blocks_for_toilet_wall1 + no_of_blocks_for_toilet_wall2

    new_toilet_wall1=user_toilet_length / brickB_length
    roundvalue7=round(new_toilet_wall1)+1
    toliet_wall1_height=room_height_const / brickB_height
    no_of_blocks_for_new_toilet_wall1=roundvalue7 * toliet_wall1_height*2

    new_toilet_wall2=user_toilet_breadth / brickB_length
    roundvalue8=round(new_toilet_wall2)+1
    toliet_wall2_height=room_height_const / brickB_height
    no_of_blocks_for_new_toilet_wall2=roundvalue8 * toliet_wall2_height * 2
    global blocks_total_for_toilet2
    blocks_total_for_toilet2=no_of_blocks_for_new_toilet_wall1 + no_of_blocks_for_new_toilet_wall2
    print("Mr/Mrs {} the total number of blocks for the toilet using smaller brick A is {:.0f} blocks and using bigger brick B is {:.0f} blocks. ".format(user_name,blocks_total_for_toilet,blocks_total_for_toilet2))
toilet_evaluation()
print("")
def final_calculation():
    #total number of blocks for all the rooms using smaller brick A 
    total_no_of_blocks=blocks_total_for_room_1 + blocks_total_for_room_2 + blocks_total_for_room_3 + blocks_total_for_toilet
    total_block_cost=brickA_cost * total_no_of_blocks
    print("Cost of brick A is 600naira..")
    print(" Therefore Mr/Mrs {} the total number of blocks used for the four rooms is: {:.0f} blocks and the cost/expense using smaller brick A is: {:.0f} Naira".format(user_name,total_no_of_blocks,total_block_cost))
    print("")
    #total number of blocks for all the rooms using bigger brick B
    total_no_of_blocks_forbrickB=blocks_total_for_first_room + blocks_total_for_second_room + blocks_total_for_third_room + blocks_total_for_toilet2
    total_block_costforbrickB=brickB_cost * total_no_of_blocks_forbrickB
    print("Cost of bigger brick B is 1000naira..")
    print(" Therefore Mr/Mrs {} the total number of blocks used for the four rooms is: {:.0f} blocks and the cost/expense using bigger brick B is: {:.0f} Naira".format(user_name,total_no_of_blocks_forbrickB,total_block_costforbrickB))

    print("")
    print("Given that the total number of blocks required for the buiding using smaller brick A is: {:.0f} blocks and total number of blocks using bigger brick B is: {:.0f} blocks".format(total_no_of_blocks,total_no_of_blocks_forbrickB))
    print("and the total cost for brickA is {:.0f} naira and the total cost for brickB is {:.0f} naira".format(total_block_cost,total_block_costforbrickB))
    print("which do you prefer Mr/Mrs {}".format(user_name))
final_calculation()