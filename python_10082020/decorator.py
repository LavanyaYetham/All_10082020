#!/usr/local/bin/python3.8
def lowercase(function):
    def wrapper():
        fun=function()
        string=fun.lower()
        return(string)
    return wrapper
def split_decorator(function):
    def wrapper():
        fun=function()
        output=fun.split()
        return (output)
    return wrapper
@split_decorator
@lowercase
def hello():
    return 'HELLO World'
print (hello())
