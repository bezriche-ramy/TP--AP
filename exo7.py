def isLeapYear(year):
    if year%4==0 :
        return True
    if year%100==0 and year%400==0:
        return True
    else:
        return False
    
year=int(input("Please type in a year: "))
if(isLeapYear(year)):
    print(year, "That year is a leap year.")
else:
    print(year,"That year is not a leap year.") 
