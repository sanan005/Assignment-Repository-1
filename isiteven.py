"""Write a program that tests if a value is even or odd. Follow the instructions outlined below:

Instructions:
The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function.

"""

value=int(input("enter a number"))
if value%2==0:
    print("The user value is an even number")
else :
    print("The user value is an odd number")