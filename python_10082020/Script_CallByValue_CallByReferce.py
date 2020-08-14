#!/usr/local/bin/python3.8
#Diff b/w call by value and call by reference
#Call by value : In the event of passing an arguments like numbers, strings and tuples to a function, the passing is like a "call by value" because we can't change the value of immutable objects being passed to the function.
#Call by reference : passing mutable objects to the function can be considered as a call by reference because their values can be changed the inside the function.

string="hello"
def print_out(string):
    string="Hi"
    print (string)
print_out(string)
print(string)

a=[10,20,30,40]
def list_out(a):
    a.append(50)
    print (a)
list_out(a)
print (a)
