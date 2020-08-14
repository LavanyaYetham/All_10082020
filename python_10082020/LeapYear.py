#!/usr/local/bin/python3.8
'''
A year, occurring once every four years, which has 366 days including 29 February as an intercalary day.
'''
Year=int(input("Please enter the Year: "))
if Year%4 == 0:
    if Year%100 == 0:
        if Year%400 == 0:
            print (Year,"is Leap Year")
        else:
            print (Year,"is not Leap Year")
    else:
        print (Year,"is Leap Year")
else:
    print (Year,"is not Leap Year")
