#!/usr/local/bin/python3.6

import re

txt="The rain in Spain"
a=re.search("^The.*Spain$",txt)
if a:
    print("YES! We have a match!")
else:
  print("No match")

b=re.findall("ai",txt)
print (b)
c=re.search("\s",txt)
print ("The first white-space character is located in position:",end="")
print (c.start())
d=re.split('\s', txt)
print(d)
e=re.split('\s', txt,1)
print(e)
f=re.sub("\s","@",txt)
print (f)
g=re.sub("\s","@",txt,2)
print (g)
h=re.search("ai",txt)
print (h)

print ("################################")
##Search for an upper case "S" character in the beginning of a word, and print its position
x=re.search(r"\bS\w+", txt)
print(x.span())
#The string property returns the search string
print (x.string)
#Search for an upper case "S" character in the beginning of a word, and print the word:
print (x.group())








