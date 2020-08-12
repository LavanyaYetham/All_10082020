#!/usr/local/bin/python3.8
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print(n,"is a Perfect number")
else:
    print(n," is not a Perfect number!")
print ("************")
S=int(input("Please enter the starting Range: "))
E=int(input("Please enter the ending Range: "))
for num in range(S,E+1):
    sum1 = 0
    for i in range(1, num):
        if(num%i == 0):
            sum1 = sum1 + i
    if (sum1 == num):
        print(num,"is a Perfect number")

