"""Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. 
The correct password is defined as 12345. The program should keep asking the user to 
enter the password until they provide the correct one.
Basic Requirements:
Define the correct password.
Use a while loop to repeatedly ask the user for the password until the correct one is entered.
Output an appropriate message when the correct password is entered.
Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""

passw=12345

maximum=5
attempts=0
while attempts<maximum:
    enter=int(input("Enter the system password"))
    if enter==passw:
        print("Entry granted!")
        break
    else:
        attempts+=1
        print("your entry is denied! your remaining attempts are",maximum-attempts)
if attempts==maximum:
    print("Maximum Attempts Reached!, You no longer have attempts remaining ")

