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

