#!/usr/local/bin/python3.8
List=[1,-2,3,4,6]
even=0
odd=0
negative=0
for i in List:
    if i > 0:
        if i%2 == 0:
            even=even+i
        else:
            odd=odd+i
    else:
        negative=negative+i
print ("List is:",List)
print ("Sum of Even Number From List: ",even)
print ("Sum of Odd Number From List: ",odd)
print ("Sum of Negative Number From List: ",negative)
