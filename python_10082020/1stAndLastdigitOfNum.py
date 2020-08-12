#!/usr/local/bin/python3.8
number=int(input("Please enter the number: "))
first_digit=number
while (first_digit >= 10):
    first_digit=first_digit // 10
print ("First digit of ",number ,"is ",first_digit)

last_digit=number%10
print ("Last digit of ",number," is ",last_digit)
