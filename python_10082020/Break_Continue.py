#!/usr/local/bin/python3.8
#Break:-It will Skip the current flow bases on condition and continue with next flow
String="I Love Python"
Len=len(String)
for i in range(Len):
    if String[i] == "y":
        break
    print (String[i],end="")
print ()
print ("********")
#Continue:-It will Skip the current iteration based on condition and continue with next iteration
a="I Love Python"
L=len(a)
for j in range(L):
    if a[j] == "y":
        continue
    print (a[j],end="")
print ()
print ("*********")
#Pass:-Pass the any statement without giving error while running the code(Pass is used to create empty function/statement)
for k in range(5):
    pass
