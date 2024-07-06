#  2) Create a program that checks if a given year is a leap year and prints the result. 
# A year is a leap year if it is divisible by 4.
# However, if the year is divisible by 100, it is not a leap year, unless:
# The year is also divisible by 400, in which case it is a leap year.
year=int(input("Enter your year "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):{
    print(year," is a leap year.")}
else:
    print(year," is not a leap year.")