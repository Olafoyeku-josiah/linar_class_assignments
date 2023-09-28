#using the addition assignment +=
def class_schedule():
    """this functions asks the user for the total number of students in class
    conditions were set that if number of students are 1 or 2 then the user(instructor)
    should wait for about 30 minutes for other students before he can start the class"""
    print("This is a function which helps the user decide if the class should start with a certain number of students in class or not")
    total_students=int(input(" Enter the number of students present in python class currently: "))
    time_frame=input(" Enter the time for the python class(e.g 10:00): ")
    if total_students in range(1,3) and time_frame==time_frame:
        print("  Wait for like 30 minutes for the rest of the students.")
        after_30mins=int(input( "if after 30 mins, Enter the number of students that entered: "))
        if after_30mins:
            after_30mins+=total_students
            """in line 13 the addition augmented operator was used to calculate total students
            in class after 30 mins through the use of the nested if conditional statement"""
            print(" Since after 30 mins total number of students in class is {} ,you can start the class properly. ".format(after_30mins))
    elif total_students in range(3,6) and time_frame==time_frame:
        print(" since total students in class is greater than 2 ,You can start the class properly and look at pending assignments")
    else:
        print("Reach out to the rest of the students.")
    #return after_30mins,total_students

#using the subtraction assignment-=
def shopping_cart():
    """ lets say you have a shopping cart and you want to keep track of the total cost of the items in your
    cart you start with an initial cost and as you remove items from your cart , you 
    can use the subtraction assignment to update the total cost."""
    #initial total cost of items in the shopping cart
    total_cost=100.0

    #removing an item from the cart
    item_price=20.0
    total_cost-=item_price
    #updating the total cost after removal of another item
    another_item_price=15.0
    total_cost-=another_item_price

    return f'The updated total cost is:{total_cost}naira'
    #return total_cost

#using the multiplication assignment *=
def total_revenue():
    """let's say you are organizing a bake sale and you want to calculate the total
    revenue based on the number of items sold and their individual prices. You can use the multiplication
    assignment to update the total revenue as you sell more items"""
    print(" This function calculates total revenue for items sold and their individual prices")
    total_revenue=0.0
    #selling cookies
    cookie_price=100.0
    num_cookies_sold=5
    total_revenue=cookie_price*num_cookies_sold
    return f'The total revenue for the cookies is {total_revenue}naira'
    #return total_revenue

#using the exponential assignment **=
def power_function():
    """the variable initial value stores the base value which is an integer and the variable power value stores the 
     exponential value which the base value would be raised to through the use of the exponential
     assignment"""
    print(" This function calculates/ raises the initial value(base value) to a certain power")
    initial_value=int(input(" enter the initial value: ")) # initial value 
    power_value=int(input(" enter the power value: ")) # power to raise x to
    initial_value**=power_value # using the exponentiation assignment
    return f'The final result using the exponential assignment is {initial_value}'

#using the floor division assignment //=
def team_event():
    """lets say you are organizing a team event and you want to distribute a certain amount of snacks equally
    among the team members.this function will calculate number of snacks 
    each team member will receive using the floor division assignment //="""
    print(" This function calculates total number of snacks available for each member in a team event.")
    total_snacks=50#total number of snacks available
    print(" The total snacks for the event is 200 snacks.")
    num_team_members=int(input("Enter the number of members in a team: ")) # number of members in a team
    total_snacks//=num_team_members
    return f'The total snacks for each member in a team is: {total_snacks}snacks per member '

#using the division assignment /=
def team_tasks():
    """lets say you have a team of 8 people and they want to complete 100 tasks in total.You want to distribute the tasks among
    the team members using the division assignment operator"""
    print("This function helps calculate/specify number of tasks given to each member in a group")
    total_tasks=100
    team_members=8
    total_tasks/=team_members
    """after executing this code the variable "task per member" will hold the 
    value of 12.5 however, since you cant assign a fraction of a task to a user you can round it down using the floor division assignment"""
    total_tasks//=1# each team member should be assigned 12 tasks
    print(" We have about 8 members in a team and 100 tasks ,we want to distribute these tasks to members of the team")
    return f'we divide total tasks by the team members .Therefore,the total task for each member is {total_tasks}tasks'

#we could create a function that would deal with user choice i.e, the user has the opportunity to interact with whatever function
def main_function_choice():
    print(" This code was written to solve different real-life scenarios using 6 different augmented operators")
    print("select a problem to continue..")
    print("1 for class schedule using addition assignment(+=)")
    print("2 for shopping cart using subtraction assignment(-=) \n3 for total revenue using multiplication assignment(*=)")
    print("4 for the power function using the exponential assignment(**=)\n5 for the team event using the floor division assignment(//=)")
    print("6 for the team tasks using both floor division and division assignments(/=) ")
    function_choice=input(" Enter either 1,2,3,4,5 or 6: ")
    if function_choice=="1":
        print(class_schedule())
    elif function_choice=="2":
        print(shopping_cart())
    elif function_choice=="3":
        print(total_revenue())
    elif function_choice=="4":
        print(power_function())
    elif function_choice=="5":
        print(team_event())
    elif function_choice=="6":
        print(team_tasks())
    else:
        print(" Pls enter a valid choice either 1,2,3,4,5,6")
main_function_choice()
