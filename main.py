# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def leap_year_identifier(year):
    # first we have to know if the year is less than 100
    if year < 100:
        #if yes then we see if the year is evenly divisible by 4
        if year % 4 == 0:
            return True
        else :
            return False
    else:
    #if no then we have to check if it's evenly divisible by (4,100,400)
        if year % 4 == 0 :
            if year % 100 ==0 :
                if year % 400 ==0:
                    return True
                else :
                    return False
            else :
                return False
        else :
            return False
year = int(input("please enter the year to identify if it's a leap year or not :"))
print(leap_year_identifier(year))


