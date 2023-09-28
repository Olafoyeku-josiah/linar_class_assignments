#string method
#1.using the capitalize method to modify the user's first and last name
first_name=input(" Enter your first name: ")
last_name=input(" Enter your last name: ")
print("hello {} {}".format(first_name.capitalizeh(),last_name.capitalize()))

#2.using the encode method to eencode hello world into bytes
message="hello world"
encoded_message=message.encode("utf-8")
print(encoded_message)

#3.using the endswith method to check the extension of a file and file type
file_name=input("Enter a file name and file extension e.g(string_method.py): ")
if file_name.endswith(".txt"):
    print("This is a text file.")
elif file_name.endswith(".py"):
    print(" This is a python file.")
else: 
    print("this is neither a text file or a python file") 

#4.using the find() method to search for the index of a word in a sentence
sentence="The quick brown fox jumps over the lazy dog."
word="fox"
index=sentence.find(word)
print("The word:",word,"starts at index:",index)

#5.using the count method to check the number of times a particular substring occurs in string
sentence="how much wood would a woodchuck chuck if a woodchuck could chuck wood"
substring="wood"
#we want to find out how many times the word wood occurs in the sentence above
word_count=sentence.count(substring)
print("The substring {} occurs {} times in the sentence".format(substring,word_count))