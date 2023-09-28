#using the get method for a mini chat bot
"""automated_response={"greeting":"hello how are you doing today?","response":"what can i help you with?"}
print("welcome to my mini chatbot")
user_name=input(" Enter your name: ")
user_greeting=input(" Enter a greeting e.g(hello): ")
if user_greeting=="hello":
    print(automated_response.get("greeting"))
    print(automated_response.get("response"))
else:
    print("enter hello.")"""

#using the keys method to return the list of all the keys in a dictionary
name_of_students={"student1":"emmanuel","student2":"samuel","student3":"simeon"}
name_of_students.keys()
print(name_of_students)

#using the pop method to remove a key-value pair inserted into a dictionary
food_items={"food item1":"bread","food item2":"beans"}
food_items.pop("food item1")
print(food_items)

#using the popitem method to remove the last key-value pair inserted into a dictionary
food_items={"food item1":"bread","food item2":"beans"}
food_items.popitem()
print(food_items)

#using the update method to update the dictionary with new key value pairs
food_items={"food item1":"bread","food item2":"beans"}
food_items.update({"food item3":"soya beans"})
print(food_items)

#using the clear method to remove all key-value pairs from the dictionary
name_of_students={"student1":"emmanuel","student2":"samuel","student3":"simeon"}
name_of_students.clear()
print(name_of_students)

#using the len method to return the number of key-value pairs in a dictionary
name_of_students={"student1":"emmanuel","student2":"samuel","student3":"simeon"}
length=len(name_of_students)
print(length)

#using the copy method to create a shallow copy of the dictionary
food_items={"food item1":"bread","food item2":"beans"}
new_food_items=food_items.copy()
print(new_food_items)