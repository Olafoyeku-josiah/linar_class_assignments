#using the append method to add values to an empty list 
my_list=[]
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print(my_list)

#using the extend method to extend the values of a list
course_outline=["maths","english","biology",]#user course outline before 200 level
course_outline.extend(["geography","physics","anatomy"])#user course outline after 200level
print(course_outline)

#using the insert method to add a certain number at a specific index
numbers=[1,2,3,4,5,6]
numbers.insert(6,7)
print(numbers)

#using the remove method to remove a specific number from a list
numbers=[1,2,3,4,5,6]
numbers.remove(1)
print(numbers)

#using the pop method to remove and return an element at a specific index from the list
food_list=["bread","beans","avocados","canola oil"]
food_list.pop(-1)
print(food_list)

#using the sort method to sort the list items in ascending order
word_list=["wood","wood","dam","institute"]
word_list.sort()
print(word_list)

#using the len method to return the number of elements in a list
word_list=["wood","wood","dam","institute"]
length=len(word_list)
print(length)

#using the reverse method to reverse the order of elements in a list
decimal_list=[3.5,6.7,8.9,9.0]
decimal_list.reverse()
print(decimal_list)
