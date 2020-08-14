#!/usr/local/bin/python3.8
string="Welcome To India"
print (string)
a=string.swapcase()
print (a)
print ("#########Another Way##########")
def swap_case(s):
     return s.swapcase()
if __name__ == '__main__':
    s = input("Enter the String: ")
    result = swap_case(s)
    print(result)
