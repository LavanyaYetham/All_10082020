#!/usr/local/bin/python3.8
"""
2's Complement 
2's Complement=1's comlement+1
"""
a=12
x=~a
print (x) 
print (bin(x))
print ("############")
num1=12
num2=13
"""
Bitwise And(&)
x y  o/p
0 0  0
0 1  0
1 0  0
1 1  1
"""
print (num1 & num2) #Bitwise And(&)
"""
Bitwise Or (|)
x y  o/p
0 0  0
0 1  1
1 0  1
1 1  1
"""
print (num1 | num2) #Bitwise Or (|)
"""
XOR:-The  1's Value of bit count is odd then result is True
x y  o/p
0 0  0
0 1  1
1 0  1
1 1  0
"""
print (num1 ^ num2)
#Left Shift(<<)
print (10<<2)
#Right Shift(>>)
print (10>>2)


