"""Write a program that tells a user how many days there are in a specific month. 
Use a dictionary to map the month numbers (1-12) to the number of days in each month."""

#Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.

month_days={
1:31,
2:29,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31,
}
    
month=int(input("enter a month number from 1 to 12:"))      #input a month number

if month>=1 and month<=12:                                  #to check if it is valid
    if month==2:
        year=int(input("enter the year:"))                                  # to check for leap year
        if year % 4 == 0 and year % 100 != 0:
            print("the given year is a leap year with february having 29 days",)
        else:
            print("It is not a leap year and chosen month february has 28 days")
    else:
        print("the month has days",{month_days[month]} )
else:
    print("the value input is invalid")

   
        
      






   