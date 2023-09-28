#this function is embedded with the introduction and welcome and also user name
def introduction(user_name):
    print("Hello {}".format(user_name))
    print("Welcome to gbenro's building construction evaluation.")
    print("This program will be calculating your total number of blocks and building expenses using two different block sizes.")
    print("   Calculating number of blocks and expense required using smaller brick A and bigger brick B")
introduction(user_name=input("Enter your name pls: "))
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
    blocks_total_for_room_1=No_of_blocks_for_wall1 + No_of_blocks_for_wall2
    new_room1_wall1=user_room1_length / brickB_length
    roundvalue1=round(new_room1_wall1)+1
    room1_wall1_height=room_height_const / brickB_height
    No_of_blocks_for_new_wall1=roundvalue1 * room1_wall1_height * 2
    new_room1_wall2=user_room1_breadth /brickB_length
    roundvalue2=round(new_room1_wall2)+1
    room1_wall2_height=room_height_const / brickB_height
    No_of_blocks_for_new_wall2=roundvalue2 * room1_wall2_height * 2
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
    blocks_total_for_room_2=No_of_blocks_for_room2_wall1 + No_of_blocks_for_room2_wall2
    new_room2_wall1=user_room2_length / brickB_length
    roundvalue3=round(new_room2_wall1)+1
    room2_wall1_height=room_height_const / brickB_height
    No_of_blocks_for_new_room2_wall1=roundvalue3* room2_wall1_height *2
    new_room2_wall2=user_room2_breadth / brickB_length
    roundvalue4=round(new_room2_wall2)+1
    room2_wall2_height=room_height_const / brickB_height
    No_of_blocks_for_new_room2_wall2=roundvalue4 * room2_wall2_height * 2
    blocks_total_for_second_room=No_of_blocks_for_new_room2_wall1 + No_of_blocks_for_new_room2_wall2
    print(" The total number of blocks for room 2 using smaller block A is {:.0f} blocks and using bigger brick B is {:.0f} blocks. ".format(blocks_total_for_room_2,blocks_total_for_second_room))
room2_calculation()