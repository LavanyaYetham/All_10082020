#!/usr/local/bin/python3.6

try:
    print (x)
except:
    print ("An exception Ocuured")
print ("************************************")
try:
    print (y)
except NameError:
    print ("Variable y is not defined")
except:
    print ("Something went Wrong")

print ("************************************")

try:
    print ("Hello")
except:
    print ("Something went Wrong")
else:
    print ("Nothing went Wrong")
print ("************************************")
try:
    print (y)
except:
    print ("Something went Wrong")
else:
    print ("Nothing went Wrong")

print ("************************************")
try:
    print (x)
except:
    print ("Something went wrong")
finally:
    print ("The 'try except' block is Finished")
print ("************************************")
a=-1
try:
    if a<0:
        raise Exception("Sorry,no Number below Zero")
except:
    print ("Something went Wrong")
