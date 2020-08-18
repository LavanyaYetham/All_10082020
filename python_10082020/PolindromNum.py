#!/usr/local/bin/python3.8
'''
A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number that remains the same when its digits are reversed. ..
'''
num=int(input("Please enter the Number: "))
New=num
z=0
while int(num) > 0:
    r=int(num)%10
    q=int(num)/10
    z=r+(z*10)
    num=int(q)
if int(z) == int(New):
   print ("The Given Number",New,"is Polindrome")
else:
   print ("The Given Number",New,"is not  Polindrome")
print ("***********************")
my_str='RADAR'
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str) == list(rev_str):
    print ("The string ia a Polindrome.")
else:
    print ("The stringis not a Polindrome")
