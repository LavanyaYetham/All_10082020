#!/usr/local/bin/python3.8
startn=int(input("Please enter the starting range: "))
endn=int(input("Please enter the ending range: "))
for i in range(startn,endn+1):
    if i%2 != 0:
         print (i,"is odd number")
print ("##find odd Numbers without If Statement##")
for i in range(1,endn+1,2):
    print (i)
    
print ("##To display odd Numbers using While Loop##")
while startn <= endn:
    if startn%2 != 0:
        print (startn)
    startn=startn+1
print ("##Using Function##")
def func(start,end):
    for i in range(start,end+1):
        if i%2 != 0:
            print (i)
func(1,10)
