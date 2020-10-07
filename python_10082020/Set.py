#!/usr/local/bin/python3.6

s1={1,2,3,4}
print (s1)
s1.add(5)
print (s1)
s1.update([6,7,8])
print (s1)
print (len(s1))
#If the item to remove does not exist, remove() will raise an error.
s1.remove(4)
print (s1)
#If the item to remove does not exist, discard() will NOT raise an error.
s1.discard(5)
print (s1)
print (s1.pop())
print (s1)
s1.clear()
print (s1)
del s1
s1={"a","b","c"}
s2={1,2,3}
s3=s1.union(s2)
print (s3)
s1.update(s2)
print (s1)
