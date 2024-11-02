"""Write a program that searches for a specific string within a list of strings. 
The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , 
and your task is to search for "Sam".

Optional Requirements:
Allow the user to input the search term instead of using a predefined value.
Implement the search functionality based on user input.
"""

list=("Jake" "Zac", "Ian", "Ron", "Sam", "Dave")
search=input("enter the desired name for search in the list: ") or "sam"  

if search in list:
    print("the desired value is available in the list")
else:
    print("the desired value is not present in the list")