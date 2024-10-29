"""In this exercise, you'll create a program 
that stores and prints your name, hometown, and age to the console using a Python dictionary."""

#ADVANCED REQUIREMENT
"""Have the user input their name, hometown, and age instead of hardcoding the values. Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python? Test the program by entering a 
string value for age (e.g., "twenty"). What happens? How can you prevent this issue?"""

name=input("enter your name: ")
hometown=input("enter your hometown: ")
age=input("enter your age; ")

#Store the information (name, hometown, and age) as key-value pairs in a dictionary.

detail_dict= {
    "Name":name,
    "Hometown": hometown,
    "Age" :age
}
#Print the values on separate lines using a single print() statement.
print(detail_dict["Name"])
print(detail_dict["Hometown"])
print(detail_dict["Age"])

#Use variables with appropriate data types for each piece of information.

print(type(detail_dict))

